from fastapi import FastAPI
from models import EmailRequest
from agents import run_sales_agent
from email_sender import send_email

app = FastAPI()

@app.post("/send-email")
async def send_sales_email(data: EmailRequest):
    generated_email = run_sales_agent(data.lead_info)
    send_email(to_email=data.email, content=generated_email)
    return {"message": "Email sent successfully!", "generated_email": generated_email}
