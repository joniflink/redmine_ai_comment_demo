# Redmine AI Comment Demo

A Redmine plugin that uses a local AI model (Ollama) to analyze and suggest priority updates.

The user can review and apply AI suggestion directly from the issue view.

This plugin has been created as a part of a Master's thesis.

[FIN] Tämä plugin on luotu osana diplomityötä. Plugin ja tämä dokumentaatio on kirjoitettu englanniksi.

## Contents

1. [Features](#1-features)
2. [Requirements](#2-requirements)
3. [Quick start](#3-quick-start)
4. [Setup steps](#4-setup-steps)
5. [Usage](#5-usage)
6. [Troubleshooting](#6-troubleshooting)
7. [Known limitations](#7-known-limitations)
8. [Directory map](#8-directory-map)
9. [Architecture](#9-architecture)
10. [Development notes](#10-development-notes)

## 1. Features

- Automatic AI analysis of new issues
- Suggested priority based on issue content
- One-click "Apply AI suggestion" button
- Local AI model (no external API required)

## 2. Requirements

- Docker & Docker Compose (modern Docked Desktop includes both)
- Python 3 (for setup scripts)
    - requires `requests`
- Ollama installed locally

### 2.1. Installation links

- Docker Desktop:  
  https://www.docker.com/products/docker-desktop/

- Ollama:  
  https://ollama.com/download

- Python:  
  https://www.python.org/downloads/

**Note!**  
Linux users may need to install Docker Compose separetly depending on their Docker installation.

## 3. Quick Start

**Installing Redmine is not needed.** Redmine itself is not included in this repository. It is started automatically using the official Redmine Docker image via Docker Compose.

---

### 3.1. Clone repo, copy `.env` and build

1. Clone repo

```bash
git clone <repo>
```

2. Navigate to repo

```bash
cd <repo>
```

3. copy `.env`

```bash
cp .env.example .env
```

4. Build and start Redmine

```bash
docker compose up -d --build
```

---

### 3.2. Open Redmine:

- Default URL: http://localhost:3000
- Default login:
    - username: admin
    - password: admin

Redmine might ask you to reset the password. You'll need to remember the password later.

Now you should have working Redmine.

Redmine can be shut down with:
```bash
docker compose down
```

and started with:
```bash
docker compose up -d
```

## 4. Setup Steps

### 4.1. Initialize Redmine default configuration

Run:

```bash
docker compose exec redmine bash -lc "cd /usr/src/redmine && bundle exec rake redmine:load_default_data RAILS_ENV=production REDMINE_LANG=en"
```

This initializes trackers, statuses, workflows and priorities. 

---

### 4.2. Configure API key

1. In Redmine go to `Administration` &rarr; `Settings` &rarr; `API`.
2. Check the box `Enable REST web service` and save.
3. Go to `My account`.
4. Find `API access key` and copy it.  
5. Paste the API key to `.env`:

```env
REDMINE_API_KEY=<Your API key here>
```

6. After updating the `.env` file, restart Redmine:

```bash
docker compose down
```
```bash
docker compose up -d
```
This will log you out of Redmine and you'll have to sign back in.

---

### 4.3. Create custom field

For the 'Apply suggestion' button to appear a custom field is needed. The custom field needs to be created manually:

In Redmine go to `Administration` &rarr; `Custom fields` &rarr; `New custom field`

- Object to attach: `Issues`

Next

- Format: `Text`  
- Name: `AI suggested priority id`  
- Trackers: all or wanted  
- Projects: all or wanted, the `For all projects` selection applies also for new projects.

If you decide to use a different name, please update `.env` and restart Redmine.

---

### 4.4. Setup Ollama

1. Ollama model (default `gemma3:1b`) can be installed and tested to work using the following command:

```bash
ollama run gemma3:1b
```

If you decide to use a different model, please update `.env` and restart Redmine.

2. Allow connections from Docker:

#### Windows

```bash
setx OLLAMA_HOST "0.0.0.0:11434"
```

#### macOS

```bash
launchctl setenv OLLAMA_HOST 0.0.0.0:11434
```

#### Linux

```bash
export OLLAMA_HOST=0.0.0.0:11434
```

---

**Note!**  
Ollama must be running before using the plugin.

**Note!**  
The plugin runs inside Docker and uses `http://ollama-host:11434`.  
The setup script run on the host and use `http://localhost:11434`.  
This is handled automatically inside the script file and requires no changes.

---

### 4.5. Run check script

You can run a check script to ensure everything is working.

```bash
python3 scripts/check_setup.py
```

The script needs `requests` to run. It can be installed by running:

```bash
pip3 install requests
```

## 5. Usage

1. Create a project
2. Create an issue.
3. The AI analysis is triggered automatically when a new issue is created.

The plugin should post a comment under the new issue. If the priority suggested by the AI differs from the current priority, a button will appear to update the priority.

## 6. Troubleshooting

- [Default data command not working](#61-default-data-command-not-working)
- [Comment doesn't appear](#62-comment-doesnt-appear)
- [The apply suggestion button doesn't appear](#63-the-apply-suggestion-button-doesnt-appear)
- [AI does not respond](#64-ai-does-not-respond)
- [Need to format Redmine](#65-need-to-format-redmine)

---

For own troubleshooting, you can view logs:

```bash
docker compose logs redmine
```

or live logs:

```bash
docker compose logs -f redmine
```

---

### 6.1. Default data command not working

In Redmine go to `Administration` and check and create data either manually or using default data links, at least in `Roles and permissions`, `Trackers`, `Issue statuses`, `Workflow` and `Enumerations / Issue priorities`.

---

### 6.2. Comment doesn't appear

Try restarting Redmine with:

```bash
docker compose down
```
```bash
docker compose up -d
```

Comments are currently generated only for new issues.

---

### 6.3. The apply suggestion button doesn't appear

The apply suggestion button should appear if the priority suggested by AI is different from the priority currently set on the issue. If the button should appear but doesn't, in Redmine go to `Administration` &rarr; `Custom fields` &rarr; `AI suggested priority id` and check that the correct trackers and project are selected.

If you've changed the name of the custom field, check that the name of the field matches in both Redmine and `.env`. Always after updating the `.env` file restart Redmine by using:

```bash
docker compose down
```
```bash
docker compose up -d
```

---

### 6.4. AI does not respond

Check Ollama is running:  
http://localhost:11434/api/tags

Ensure the model is installed:
```bash
ollama list
```

---

### 6.5. Need to format Redmine

You can delete all data from Redmine by using:

```bash
docker compose down -v
```

**WARNING:**  
This will remove the database and all Redmine data.

## 7. Known limitations

- Requires manual initial Redmine setup
- Works only with local Ollama instance
- AI suggestions are not always accurate
- No authentication between Redmine and Ollama

## 8. Directory map

Your directory should look something like this after copying the `.env`
```text
redmine_ai_comment_demo/
├── plugins/
│   └── redmine_ai_comment/
│       ├── app/
│       │   └── controllers/
│       │       └── ai_comment_controller.rb
│       ├── config/
│       │   └── routes.rb
│       ├── lib/
│       │   ├── ai_comment.py
│       │   └── ai_hook_listener.rb
│       ├── init.rb
│       └── requirements.txt
├── scripts/
│   └── check_setup.py
├── .env
├── .env.example
├── .gitignore
├── docker-compose.yaml
├── Dockerfile
└── README.md
```

## 9. Architecture

Redmine (Docker)  
→ Python script  
→ Ollama (local)  
→ AI response  
→ Redmine update 

## 10. Development notes

This project was developed as a prototype for evaluating AI-assistant project management workflows. It is not inteded for production use.