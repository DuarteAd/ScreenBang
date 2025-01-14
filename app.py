import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "Application Flask fonctionnelle !"

@app.route('/script.py', methods=['GET'])
def serve_script_py():
    return send_file("script.py", as_attachment=True)

@app.route('/script.exe', methods=['GET'])
def serve_script_exe():
    return send_file("script.exe", as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Utilise le port assigné par Heroku
    app.run(host='0.0.0.0', port=port)
