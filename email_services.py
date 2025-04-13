import os
import sendgrid
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
FROM_EMAIL = os.getenv("FROM_EMAIL", "your@email.com")

def send_email(to_email, content):
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject="Personalized Offer Just for You",
        plain_text_content=content
    )
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

print(f"{SENDGRID_API_KEY}, {FROM_EMAIL} ")