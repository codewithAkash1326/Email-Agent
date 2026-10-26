
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from langchain_core.tools import tool
load_dotenv()

print("GMAIL_USER exists:", bool(os.getenv("GMAIL_USER")))
print("GMAIL_APP_PASSWORD exists:", bool(os.getenv("GMAIL_APP_PASSWORD")))



def send_email_by_gmail(receiver_email: str, subject: str, body: str) -> bool:
    try:
        
        sender_email = os.environ["GMAIL_USER"]
        app_password = os.environ["GMAIL_APP_PASSWORD"]
 
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain", "utf-8"))

        
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(
                sender_email,
                receiver_email,
                message.as_string()
            )

        print("Email sent successfully!")
        return True

    except (KeyError, smtplib.SMTPException, OSError) as error:
        print(f"Failed to send email: {error}")
        return False


@tool
def send_email_tool(email:str,subject:str,body:str):
     """ Send an email using Gmail SMTP.
    
            Args:
                email: Email address of the recipient.
                subject: Subject line of the email in one line.
                body: Plain-text content of the email.
    """
     send_email_by_gmail(email , subject,body)

     return "Email send succusfully"
