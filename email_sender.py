import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SENDER_EMAIL, SENDER_PASSWORD
from email_template import generate_email_html  # Import the HTML generation function

def send_email(recipient, subject, body):
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient
        msg['Subject'] = subject

        # Split the body into summary and precautions
        parts = body.split("Precautionary Steps:")
        summary = parts[0].strip().split("\n")[1:]  # Remove "Summary:" and get the rest
        precautions = parts[1].strip().split("\n") if len(parts) > 1 else []

        # Use the HTML content from the new module
        html = generate_email_html(subject, summary, precautions)

        # Attach both plain text and HTML versions
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(html, 'html'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False
