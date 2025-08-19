# Reddit Job Notification Bot 📬

A Python bot that scans job subreddits and emails you when posts match your keywords (e.g., “Python” + “remote”). Runs automatically with GitHub Actions.

## Features
- Monitors multiple subreddits
- Keyword filters (edit in `main.py`)
- Email alerts
- Daily automation via GitHub Actions

## How It Works
1) GitHub Actions installs deps from `requirements.txt`  
2) Injects your secrets (no hardcoding)  
3) Runs `main.py` and exits

## Setup
1. Add repo **Secrets** (Settings → Secrets and variables → Actions):  
   `CLIENT_ID, CLIENT_SECRET, USER_AGENT, EMAIL_ADDRESS, EMAIL_PASSWORD, TO_EMAIL`
2. Ensure files exist:
