import os
import requests

REDMINE_BASE_URL = os.getenv("REDMINE_BASE_URL", "").rstrip("/")
REDMINE_API_KEY = os.getenv("REDMINE_API_KEY")
FIELD_NAME = os.getenv("AI_PRIORITY_CUSTOM_FIELD_NAME")

# Prints

def print_fail(message, indent = 0):
    print(f"{' '*indent}FAIL: {message}")

def print_ok(message, indent = 0):
    print(f"{' '*indent}OK:   {message}")

#

def check_env():
    ok = True
    
    if REDMINE_BASE_URL == "":
        print_fail("REDMINE_BASE_URL not found.")
        ok = False

    if not REDMINE_API_KEY:
        print_fail("REDMINE_API_KEY not found.")
        ok = False

    if not FIELD_NAME:
        print_fail("AI_PRIORITY_CUSTOM_FIELD_NAME not found.")
        ok = False
    
    if not ok: print("Please check .env")

    return ok

def get_custom_fields():
    response = requests.get(
        f"{REDMINE_BASE_URL}/custom_fields.json?key={REDMINE_API_KEY}",
        timeout = 60
    )
    response.raise_for_status()
    return response.json().get("custom_fields", [])

def create_custom_field():
    payload = {
        "custom_field": {
            "name": FIELD_NAME,
            "field_format": "string",
            "is_required": False,
            "visible": True,
            "editable": True,
            "type": "IssueCustomField"
        }
    }
    
    response = requests.post(
        f"{REDMINE_BASE_URL}/custom_field.json?key={REDMINE_API_KEY}",
        json = payload,
        timeout = 60
    )

    if response.status_code >= 400:
        print_fail(f"Could not create custom field: {response.status_code} {response.text}")
    else:
        print_ok(f"Created custom field: {FIELD_NAME}")

# Main

def main():
    print("\nCreating custom field")
    if not check_env(): return

    existing = get_custom_fields()
    for field in existing:
        if field.get("name") == FIELD_NAME:
            print_ok(f"Custom field already exists: '{FIELD_NAME}' (id: {field.get('id')})\n")
            return
        
    create_custom_field()
    print()

if __name__ == "__main__":
    main()
