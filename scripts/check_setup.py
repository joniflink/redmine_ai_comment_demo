import os
import sys

import requests

REDMINE_BASE_URL = os.getenv("REDMINE_BASE_URL", "").rstrip("/")
REDMINE_API_KEY = os.getenv("REDMINE_API_KEY")
OLLAMA_URL = os.getenv("OLLAMA_URL", "").rstrip("/")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
AI_PRIORITY_CUSTOM_FIELD_NAME = os.getenv("AI_PRIORITY_CUSTOM_FIELD_NAME")

# Prints

def print_fail(message, indent = 0):
    print(f"{' '*indent}FAIL: {message}")

def print_ok(message, indent = 0):
    print(f"{' '*indent}OK:   {message}")

def print_warning(message, indent = 0):
    print(f"{' '*indent}WARN: {message}")

# Checks

def check_env():
    print("Checking .env")
    success = {"redmine": True, "Ollama": True, "cf": True}
    all_successful = True

    if REDMINE_BASE_URL == "":
        print_fail("REDMINE_BASE_URL not found", 2)
        success["redmine"] = False
        all_successful = False

    if not REDMINE_API_KEY:
        print_fail("REDMINE_API_KEY not found.", 2)
        success["redmine"] = False
        all_successful = False

    if OLLAMA_URL == "":
        print_fail("OLLAMA_URL not found.", 2)
        success["Ollama"] = False
        all_successful = False

    if not OLLAMA_MODEL:
        print_fail("OLLAMA_MODEL not found.", 2)
        success["Ollama"] = False
        all_successful = False

    if not AI_PRIORITY_CUSTOM_FIELD_NAME:
        print_fail("AI_PRIORITY_CUSTOM_FIELD_NAME not found.", 2)
        success["cf"] = False
        all_successful = False
    
    if all_successful: print_ok(".env loaded successfully.", 2)
    print()
    return success

def check_redmine_api():
    print("Checking API")

    data = redmine_get("/users/current.json")

    if not data: return False

    login = data.get("user", {}).get("login", "unknown")

    print_ok(f"Redmine API connection successful. Current user: {login}\n", 2)
    return True

def check_trackers():
    print("Checking trackers")
    
    trackers_json = redmine_get("/trackers.json")

    if not trackers_json: return False

    trackers = trackers_json.get("trackers")

    if not trackers:
        print_fail("No trackers found. Run Redmine default data setup.\n", 2)
        return False
    
    print_ok(f"Trackers found: {', '.join(t['name'] for t in trackers)}.\n", 2)
    return True

def check_prios():
    print("Checking issue priorities")

    prio_json = redmine_get("/enumerations/issue_priorities.json")

    if not prio_json: return False

    prios = prio_json.get("issue_priorities")

    if not prios:
        print_fail("No issue priorities found. Run Redmine default data setup.\n", 2)
        return False
    
    print_ok(f"Issue priorities found: {', '.join(p['name'] for p in prios)}.\n", 2)
    return True

def check_custom_field():
    print("Checking custom field")

    fields_json = redmine_get("/custom_fields.json")

    if not fields_json: return False
    
    fields = fields_json.get("custom_fields", [])

    for field in fields:
        if field.get("name") == AI_PRIORITY_CUSTOM_FIELD_NAME:
            print_ok(f"Custom field found: '{field.get('name')}' (id: {field.get('id')}).\n", 2)
            return True
        
    print_fail(f"Custom field not found: '{AI_PRIORITY_CUSTOM_FIELD_NAME}'. Run scripts/create_custom_field.py.\n", 2)
    return False

def check_ollama():
    print("Checking Ollama")

    try:
        response = requests.get(
            f"{normalize_ollama_url(OLLAMA_URL)}/api/tags",
            headers = {"Host": "localhost:11434"},
            timeout = 60
        )
    except requests.RequestException as exc:
        print_fail(f"Could not connect to Ollama at '{OLLAMA_URL}': {exc}\n", 2)
        return False
    
    if response.status_code >= 400:
        print_fail(f"Ollama responded with {response.status_code} {response.text}\n", 2)
        return False
    
    models = [m.get("name") for m in response.json().get("models", [])]

    if OLLAMA_MODEL not in models:
        print_warning(f"Ollama works, but model '{OLLAMA_MODEL}' was not found.\n{' '*8}Run: ollama run {OLLAMA_MODEL}\n", 2)
    else:
        print_ok(f"Ollama works and model '{OLLAMA_MODEL}' is available.\n", 2)

    return True

# 

def redmine_get(path):
    url = f"{REDMINE_BASE_URL}{path}?key={REDMINE_API_KEY}"
    response = requests.get(url, timeout = 60)

    if response.status_code >= 400:
        print_fail(f"Redmine API request failed: {path}: {response.status_code} {response.text}\n", 2)
        return None
    
    return response.json()

def normalize_ollama_url(url):
    return url.replace("http://ollama-host:", "http://localhost:")

# Main

def main():
    fails = 0

    print("\nChecking setup...\n")
    
    env_return = check_env()

    if env_return["redmine"]:
        if check_redmine_api():
            if not check_trackers(): fails += 1
            if not check_prios(): fails += 1
            if env_return["cf"]:
                if not check_custom_field(): fails += 1
            else:
                print_fail("Custom field not checked, need .env AI_PRIORITY_CUSTOM_FIELD_NAME\n")
                fails += 1
        else:
            for check in ["Trackers", "Issue priorities", "Custom field"]:
                print_fail(f"{check} not checked, need API")
            fails += 4
            print()
    else:
        for check in ["API", "Trackers", "Issue priorities", "Custom field"]:
            print_fail(f"{check} not checked, need .env REDMINE")
        fails += 5
        print()

    if env_return["Ollama"]:
        if not check_ollama(): fails += 1
    else:
        print_fail("Ollama not checked, need .env OLLAMA\n")
        fails += 1

    if fails == 6:
        print("All checks failed.")
    elif fails > 0:
        print(f"{fails} check{'s' if fails > 1 else ''} failed.")
    else:
        print("All checks successful.")
    print()

if __name__ == "__main__":
    main()
