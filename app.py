import os
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return "Application Flask fonctionnelle !"

@app.route('/files/<filename>', methods=['GET'])
def serve_file(filename):
    try:
        # Vérifie si le fichier demandé existe et le renvoie
        return send_file(filename, as_attachment=True)
    except FileNotFoundError:
        return f"Le fichier {filename} est introuvable.", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Utilise le port assigné par Heroku
    app.run(host='0.0.0.0', port=port)
