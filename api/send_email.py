import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(event, context):
    to_email = event['queryStringParameters']['to']
    subject = event['queryStringParameters']['subject']
    message = event['queryStringParameters']['message']

    from_email = "daoudaabassichristian@gmail.com"
    password = os.getenv('418-A18-504@.com')  # Ajoutez votre mot de passe d'application

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        return {
            'statusCode': 200,
            'body': 'Email sent successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
