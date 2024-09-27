from flask import Flask, request, jsonify
from autorizador import create_app
import requests
import jwt
import datetime


app = create_app('default')
app_context = app.app_context()
app_context.push()

SECRET_KEY = app.config['JWT_SECRET_KEY']
ALGORITHM = app.config['ALGORITHM']

users = {
    'user1': '1234'
}


@app.route('/validate', methods=['POST'])
def validate_user():
    """
    Function para validar el usuario con sus respectivas caracteristicas
    """
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    if username in users and users[username] == password:
        # Generar JWT
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm=ALGORITHM)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    

@app.route('/validateToken', methods=['POST'])
def validate_token():
    """
    Function para realizar validacion del token cifrandolo.
    """
    token_recibido = request.get_json()
    token = None
    if token_recibido:
        token = token_recibido.split(' ')[1]
    token_guardado = token
    try:
        payload = jwt.decode(token_guardado, SECRET_KEY, algorithms=[ALGORITHM])
        return jsonify({'mensaje': 'Token válido', 'payload': payload}), 200
    except jwt.InvalidTokenError:
        return jsonify({'mensaje': 'Token inválido o modificado'}), 401