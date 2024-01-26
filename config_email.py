from redmail import EmailSender
from pathlib import Path

def send_email_config():
    # Récupérer le chemin du script actuel
    script_path = Path(__file__).resolve()
    # Récupérer le chemin du répertoire parent du script (le répertoire contenant le script)
    parent_directory = script_path.parent
    # Joindre le chemin relatif du fichier de log
    log_file_path = parent_directory / "flask/app.log"
    email = EmailSender(
        host="smtp.gmail.com",
        port=587,
        username="lombardi.joachim@gmail.com",
        password="brig hcvw ofhe oqxy",
    )
    return log_file_path, email