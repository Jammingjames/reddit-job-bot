# Reddit Job Bot 🤖

This bot scans job-related subreddits (like **r/forhire**, **r/slavelabour**, **r/hireaprogrammer**, and **r/RemoteJobs**) for new posts that mention **Python** and **remote work**.
When it finds one, it sends an **email alert** so you never miss an opportunity 🚀.

---

## 🔧 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/<Jammingjames>/reddit-job-bot.git
cd reddit-job-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your secrets (environment variables)

Create a `.env` file locally (not committed to GitHub):

```
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
USER_AGENT=your_user_agent
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
TO_EMAIL=recipient_email@gmail.com
```

> ⚠️ These secrets are already stored safely in GitHub Actions under **Repository → Settings → Secrets** for production.

### 4. Run the bot locally

```bash
python main.py
```

---

## 🤖 Run on GitHub Actions

This project comes with a workflow (`.github/workflows/bot.yml`) that runs the bot on GitHub’s servers.
That means the bot can keep running **even if your computer is off** 🎉.

---

## 📬 Example Email Alert

When a matching job is found:

```
Subject: New Python Job: Need Python Dev for Remote Work
Body:
Need Python Dev for Remote Work

Link: https://reddit.com/r/forhire/...
```

---

## 🛡️ Security Notes

* Secrets like Reddit API keys and email credentials are **never hard-coded** in the repo.
* They are stored securely in GitHub Actions Secrets.
* The code is safe to share publicly.

