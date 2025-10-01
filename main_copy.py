import os
import praw
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time  # Import the time module

# --- FUNCTION MOVED UP ---


def send_email(subject, body):
    from_email = "jamesedgal00@gmail.com"
    to_email = "jamesedgal00@gmail.com"
    password = "cjpsfkmhuyftbtlv"
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)
            print("📧 Email alert sent!")
    except Exception as e:
        print("❌ Failed to send email:", e)


# --- REDDIT CONNECTION ---
reddit = praw.Reddit(
    client_id="tc7THF2UDjKaowUIVBR9WA",
    client_secret="iH1QpslxMY-H5TmH7K-5APEZeFttKw",
    user_agent="job bot by u/ Ruoski999"
    )

# Test the connection by printing your Reddit username
try:
    # might print None if not logged in
    print("Connected to Reddit as: ", reddit.user.me())
    send_email("✅ Bot Started", "Your Reddit job bot is now running locally!")
except Exception as e:
    print("Error connecting to Reddit: ", e)

seen_posts = set()  # keep track of posts already seen to avoid duplicates
subreddits = ['forhire', 'slavelabour', 'hireaprogrammer', 'Remotejobs']


def check_for_jobs():  # define the function to check for new job postings
    print("Checking for new job posts...\n")

    for name in subreddits:
        subreddit = reddit.subreddit(name)
        print(f"Searching r/{name}")
        for posts in subreddit.new(limit=10):  # limit to 10 new posts
            title = posts.title.lower()
            if posts.id not in seen_posts:
                if "python" in title and ("remote" in title or "work from home" in title):
                    print("Job Found!")
                    print("Title: ", posts.title)
                    print("Link: ", posts.url)
                    print("--" * 40)
                    # Send email
                    email_subject = f"New Python Job: {posts.title}"
                    email_body = f"{posts.title}\n\nLink: {posts.url}"
                    send_email(email_subject, email_body)
            seen_posts.add(posts.id)
while True:
    check_for_jobs()
    print("⏳ Waiting 10 seconds until next check...\n")
    time.sleep(10)
