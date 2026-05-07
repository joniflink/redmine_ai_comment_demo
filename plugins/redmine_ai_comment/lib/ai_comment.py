import json
import sys
import requests
import os


BASE_URL = os.getenv("REDMINE_BASE_URL")
API_KEY = os.getenv("REDMINE_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
AI_PRIORITY_CUSTOM_FIELD_ID = os.getenv("AI_PRIORITY_CUSTOM_FIELD_ID")

ISSUE_PRIORITIES = {}


def aiComment(issue_id):
    issue_json = getIssue(issue_id)
    issue_str = structureIssue(issue_json)
    task_str = structureTask(issue_str)
    aiResponse = messageOllama(task_str)
    current_prio = issue_json.get("priority", {}).get("id")
    structuredResponse = structureResponse(aiResponse, current_prio)
    saveAiPrioritySuggestion(aiResponse.get("suggested_priority_id"))

    if structuredResponse != None:
        addComment(issue_id, structuredResponse)


def saveAiPrioritySuggestion(priority_id):
    if priority_id != None:
        url = f"{BASE_URL}/issues/{issue_id}.json?key={API_KEY}"

        data = {
            "issue": {
                "custom_fields": [
                    {
                        "id": AI_PRIORITY_CUSTOM_FIELD_ID,
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
You're part of an automation.
Your job is to analyze an issue and suggest a priority for it.
Include a justification of the suggested priority in the comment field.
The suggested priority must match in both fields.
The comment field will be added straight to the comment which will be added under the issue.
The comment field may contain other information as well.
The end-user cannot reply to you.
Return ONLY a valid JSON in this exact format:\n
{
    "suggested_priority_id": <ID of suggested priority as integer, from the list below>,
    "comment": "<comment to show for the end-user>"
}\n
Do not include any extra text.
Your response has to be able to be parsed straihgt to JSON with Python's json.loads(your_response)\n\n
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

    return parseAiResponse(response)


def clean_json_text(text):
    text = text.strip()

    if text.startswith("```json"):
        text = text.removeprefix("```json").strip()
    if text.startswith("```"):
        text = text.removeprefix("```").strip()
    if text.endswith("```"):
        text = text.removesuffix("```").strip()

    return text


def parseAiResponse(ai_response):
    content = ai_response.json()["message"]["content"]

    try:
        return json.loads(clean_json_text(content))
    except json.JSONDecodeError as e:
        raise ValueError(f"AI did not return valid JSON: {content}") from e


def structureResponse(response_json, current_prio):
    suggested_prio = response_json.get("suggested_priority_id")
    comment = response_json.get("comment")

    response = ""

    if comment != None:
        response += "Priority suggestion from AI:\n"
        response += comment

    if suggested_prio != None:
        if len(response) != 0:
            response += "\n\n"
            response += "Suggestion: "

        if suggested_prio == current_prio:
            response += "Keep the priority as **" + getIssuePriority(current_prio) + "**."
        else:
            response += "Change the priority from " + getIssuePriority(current_prio) + " to **" + getIssuePriority(suggested_prio) + "**."

    if len(response) > 0:
        response += "\n\n- Ollama AI"
        return response
    else:
        return None
    

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
