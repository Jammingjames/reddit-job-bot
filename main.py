import os
import praw
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time # Import the time module
#connect to reddit using credentials stored in secrets 
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), user_agent=os.getenv('USER_AGENT'))
#Test the connection by printing your Reddit username 
try:
    print("Connected to Reddit as: ", reddit.user.me()) #might print None if not logged in 
except Exception as e:
    print("Error connecting to Reddit: ", e)
seen_posts = set()  #keep track of posts already seen to avoid duplicates
subreddits = ['forhire', 'slavelabour', 'hireaprogrammer', 'Remotejobs']
def check_for_jobs():  #define the function to check for new job postings
    print("Checking for new job posts...\n")
def send_email(subject, body):
    from_email = os.environ['EMAIL_ADDRESS']
    to_email = os.environ['TO_EMAIL']
    password = os.environ['EMAIL_PASSWORD']
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

    for name in subreddits:
        subreddit = reddit.subreddit(name)
        print(f"Searching r/{name}")
        for posts in subreddit.new(limit=10):  #limit to 10 new posts
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
  # Wait for 10 seconds before checking again
