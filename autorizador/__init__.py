from flask import Flask
def create_app(config_name):
    app = Flask(__name__)
    # Configurar el SECRET_KEY para JWT
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'
    app.config['ALGORITHM'] = 'HS256'
    return app