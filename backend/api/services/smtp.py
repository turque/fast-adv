import smtplib

# import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from api.settings import Settings

settings = Settings()


def send_invite(sender, team_name, receiver_name, receiver_email, token):
    message = MIMEMultipart('alternative')
    message['Subject'] = 'multipart test'
    message['From'] = sender_email = settings.SENDER_EMAIL
    message['To'] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"""\
    Olá {receiver_name},
    {sender} te convidou para participar do time {team_name}
    /api/invite/validate/{token}"""
    html = f"""\
    <html>
    <body>
        <p>Olá {receiver_name},<br>
        {sender} te convidou para participar do time {team_name}<br>
        <a href="/api/invite/validate/{token}">
            Aceitar o convite
        </a>.
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL("localhost", 143, context=context) as server:
    # server.login(sender_email, password)

    with smtplib.SMTP(host=settings.HOST, port=settings.HOST_PORT) as server:
        server.sendmail(sender_email, receiver_email, message.as_string())
