from flask import Flask, request, jsonify
from autorizador import create_app
import requests
import jwt
import datetime

app = create_app('default')
app_context = app.app_context()
app_context.push()

# Clave secreta para firmar el JWT
SECRET_KEY = app.config['JWT_SECRET_KEY']
ALGORITHM = app.config['ALGORITHM']

# Usuario simulado
users = {
    'user1': '1234'
}


@app.route('/validate', methods=['POST'])
def validate_user():
    # Obtiene las credenciales a validar
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    # Validar las credenciales
    if username in users and users[username] == password:
        # Generar JWT
        # Almacena el nombre del usuario que lo genero y la fecha de expiracion (1 hora)
        token = jwt.encode({
            'username': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm=ALGORITHM)
        
        # Devuelve el token al API_Gateway
        return jsonify({'token': token}), 200
    else:
        # Indica si las credenciales son invalidas
        return jsonify({'error': 'Invalid credentials'}), 401
    
# Valida el estado del token
@app.route('/validateToken', methods=['POST'])
def validate_token():
    # Recibe el token
    token_recibido = request.get_json()
    token = None
    if token_recibido:
        # Se extrae el token del formato "Bearer <token>"
        token = token_recibido.split(' ')[1]
    # Guardar el token en una variable
    token_guardado = token
    # Se descifra el token a partir de la SECRET_KEY
    try:
        # Si logra decifrarlo, el token es correcto
        payload = jwt.decode(token_guardado, SECRET_KEY, algorithms=[ALGORITHM])
        return jsonify({'mensaje': 'Token válido', 'payload': payload}), 200
    except jwt.InvalidTokenError:
        # Si falla en decifrarlo, el token ha sido adulterado
        return jsonify({'mensaje': 'Token inválido o modificado'}), 401