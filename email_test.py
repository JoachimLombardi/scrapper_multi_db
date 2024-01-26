from redmail import EmailSender
from pathlib import Path
from config_email import send_email_config

def send_email_log():
    log_file_path, email = send_email_config()
    email.send(
        subject="An example email",
        sender="lombardi.joachim@gmail.com",
        receivers=['lombardi.joachim@gmail.com'],
        text="Hello!",
        html="<h1>Hello!</h1>",
        attachments={
            'my_log_file.log': log_file_path.read_bytes()
        }
    )
