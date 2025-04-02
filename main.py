# main.py
from flask import Flask
from app.controllers.auth_controller import auth_bp
from dash_app.layout import init_dash

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder="app/templates")
app.secret_key = os.getenv("FLASK_SECRET_KEY")


# Registra as rotas Flask
app.register_blueprint(auth_bp)

# Inicializa o Dash (ligado ao Flask)
dash_app = init_dash(app)



if __name__ == '__main__':
    app.run(debug=True)
