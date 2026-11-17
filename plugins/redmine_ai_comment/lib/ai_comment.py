import json
import sys
import requests
import os

from duration import Duration

BASE_URL = os.getenv("REDMINE_BASE_URL")
API_KEY = os.getenv("REDMINE_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
AI_PRIORITY_CUSTOM_FIELD_NAME = os.getenv("AI_PRIORITY_CUSTOM_FIELD_NAME")

ISSUE_PRIORITIES = {}


def aiComment(issue_id):
    issue_json = getIssue(issue_id)
    issue_str = structureIssue(issue_json)
    task_str = structureTask(issue_str)
    aiResponse = messageOllama(task_str)
    structuredResponse = structureResponse(aiResponse)
    saveAiPrioritySuggestion(aiResponse.get("suggested_priority_id"))

    if structuredResponse != None:
        addComment(issue_id, structuredResponse)


def get_ai_priority_custom_field_id():
    url = f"{BASE_URL}/custom_fields.json?key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()

    fields = response.json().get("custom_fields", [])

    for field in fields:
        if field.get("name") == AI_PRIORITY_CUSTOM_FIELD_NAME:
            return field["id"]

    return None


def saveAiPrioritySuggestion(priority_id):
    field_id = get_ai_priority_custom_field_id()
    if priority_id and field_id:
        url = f"{BASE_URL}/issues/{issue_id}.json?key={API_KEY}"

        data = {
            "issue": {
                "custom_fields": [
                    {
                        "id": field_id,
                        "value": str(priority_id)
                    }
                ]
            }
        }

        print("Saving AI priority suggestion")
        print("URL:", url)
        print("Payload:", data)

        response = requests.put(url, json = data)

        print("Status:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()
    else:
        missing = []
        if not priority_id: missing.append("priority_id")
        if not field_id: missing.append("field_id")
        print(f"[ai_comment.py] AI priority suggestion not saved to Redmine: {' and '.join(missing)} missing.")


def getIssue(issue_id):
    url = f"{BASE_URL}/issues/{issue_id}.json?key={API_KEY}"
    return requests.get(url).json().get("issue")


def getProject(project_id):
    url = f"{BASE_URL}/projects/{project_id}.json?key={API_KEY}"
    return requests.get(url).json().get("project")


def getIssuePriority(priority_id):
    return getIssuePriorities().get(priority_id)


def getIssuePriorities():
    if len(ISSUE_PRIORITIES) == 0:
        updateIssuePriorities()
    return ISSUE_PRIORITIES


def updateIssuePriorities():
    url = f"{BASE_URL}/enumerations/issue_priorities.json?key={API_KEY}"
    prios = requests.get(url).json().get("issue_priorities")

    for prio in prios:
        id = int(prio.get("id"))
        name = prio.get("name")
        ISSUE_PRIORITIES[id] = name


def structureIssuePriorities():
    structured = "Priority options: (ID: Name)"
    prios = getIssuePriorities()
    for id, name in prios.items():
        structured += f"\n{id}: {name}"
    return structured


def structureProject(project_json):
    title = project_json.get("name", "Unknown")
    desc = project_json.get("description", "Unknown")

    return f"""
Project:
Title: {title}
Description {desc}
    """


def structureIssue(issue_json):
    title = issue_json.get("subject", "Unknown")
    desc = issue_json.get("description", "Unknown")
    tracker = issue_json.get("tracker", {}).get("name", "Unknown")
    project_id = issue_json.get("project", {}).get("id")

    return f"""
{structureProject(getProject(project_id))}\n
Issue:
Type: {tracker}
Title: {title}
Description: {desc}
    """


def structureTask(structuredIssue):
    structuredPriorities = structureIssuePriorities()
    return """
Analyze the following issue. Suggest a priority and a time estimate for the issue.
The suggested priority must be picked from the options below.
Parse your response as a valid JSON in the following format:

{
    "suggested_priority_id": <Priority ID as an integer>,
    "time_estimate": <Time estimate in minutes (may be over 60, will be parsed later) as an integer for the whole issue>,
    "reason": <Reason for the choices>
}

Do not include any extra text. Your response will go directly into a JSON parser.
Make sure that your response can be automatically read using Python's json.loads()\n\n
""" + structuredPriorities + "\n\n" + structuredIssue


def messageOllama(message):
    url = f"{OLLAMA_URL}/api/chat"
    response = requests.post(
        url,
        headers={"Host": "localhost:11434"},
        json={
            "model": OLLAMA_MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],
            "stream": False
        },
        timeout=60
    )
    print(response)
    return parseAiResponse(response)


def clean_json_text(text):
    text = text.strip()

    if text.startswith("```json"):
        text = text.removeprefix("```json").strip()
    if text.startswith("```"):
        text = text.removeprefix("```").strip()
    if text.endswith("```"):
        text = text.removesuffix("```").strip()

    text = text.replace("\\_", "_")

    import re
    text = re.sub(r',\s*}', '}', text)

    return text


def parseAiResponse(ai_response):
    content = ai_response.json()["message"]["content"]

    try:
        return json.loads(clean_json_text(content))
    except json.JSONDecodeError as e:
        raise ValueError(f"AI did not return valid JSON: {content}") from e



def structureResponse(response_json):
    suggested_prio = response_json.get("suggested_priority_id")
    duration = Duration(response_json.get("time_estimate"))
    reason = response_json.get("reason")

    return f"""
Suggestion from AI

Suggested priority: {getIssuePriority(suggested_prio)}
Suggested time estimate: {duration.as_string()}
Reason: {reason}
"""
    

def addComment(issue_id, text):
    url = f"{BASE_URL}/issues/{issue_id}.json?key={API_KEY}"
    data = {
        "issue": {
            "notes": text
        }
    }
    requests.put(url, json=data)


if __name__ == "__main__":
    issue_id = sys.argv[1]
    aiComment(issue_id)
