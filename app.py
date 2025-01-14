import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "Application Flask fonctionnelle !"

@app.route('/bang.py', methods=['GET'])
def serve_bang_py():
    return send_file("bang.py", as_attachment=True)

@app.route('/syshelper.py', methods=['GET'], endpoint='serve_syshelper_py')
def serve_bang2_py():
    return send_file("syshelper.py", as_attachment=True)

@app.route('/bang.exe', methods=['GET'])
def serve_script_exe():
    return send_file("bang.exe", as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Utilise le port assigné par Heroku
    app.run(host='0.0.0.0', port=port)
