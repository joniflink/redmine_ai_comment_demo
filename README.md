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

- Docker & Docker Compose
- Python 3 (for setup scripts)
    - requires `requests`
- Ollama installed locally

## 3. Quick Start

**Installing Redmine not needed.** Redmine itself is not included in this repository. It is started automatically using the official Redmine Docker image via Docker Compose.

---

### 3.1. Clone repo, copy `.env` and build

```bash
git clone <repo>
cd <repo>
cp .env.example .env
docker compose up -d --build
```

---

### 3.2. Open Redmine:

- Default URL: http://localhost:3000
- Default login:
    - username: admin
    - password: admin

Now you should have working Redmine.

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
docker compose restart redmine
```

---

### 4.3. Create custom field

For the 'Apply suggestion' button to appear a custom field is needed. You can create the custom field using the following script:

```bash
python3 scripts/create_custom_field.py
```

The script needs `requests` to run.

---

### 4.4. Setup Ollama

1. Ollama model (default `gemma3:1b`) can be installed and tested to work using the following command:

```bash
ollama run gemma3:1b
```

If you decide to use a different model, please update `.env`.

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

The script requires `requests`.

## 5. Usage

1. Create a project
2. Create an issue.
3. The AI analysis is triggered automatically when a new issue is created.

The plugin should post a comment under the new issue. If the priority suggested by the AI differs from the current priority, a button will appear to update the priority.

## 6. Troubleshooting

### 6.1. Default data command not working

In Redmine go to `Administration` and check and create data either manually or using default data links, at least in `Roles and permissions`, `Trackers`, `Issue statuses`, `Workflow` and `Enumerations / Issue priorities`.

---

### 6.2. Custom field script not working

You can create the custom field manually:

Go to `Redmine` &rarr; `Administration` &rarr; `Custom fields` &rarr; `New custom field`

Object to attach: `Issues`

Format: `Text`  
Name: `AI suggested priority id` 

If you decide to use a different name, please update `.env`.

---

### 6.3. AI does not respond

Check Ollama is running:  
http://localhost:11434/api/tags

Ensure the model is installed:
```bash
ollama list
```

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
│   ├── check_setup.py
│   └── create_custom_field.py
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