from flask import Flask, request, jsonify
from api_gateway import create_app
import requests

app = create_app('default')
app_context = app.app_context()
app_context.push()

# URL del microservicio autorizador
AUTHORIZER_URL = 'http://localhost:5003'  # Cambia al puerto donde esté corriendo el microservicio

@app.route("/")
def home():
    return "Hello World, from Flask!"

@app.route('/login', methods=['POST'])
def login():
    # Obtener las credenciales del cuerpo de la solicitud
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    try:
        # Enviar las credenciales al microservicio autorizador
        response = requests.post(f"{AUTHORIZER_URL}/validate", json=user_data)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Obtener el JWT generado por el microservicio
            jwt_token = response.json().get('token')
            if jwt_token:
                return jsonify({'token': jwt_token}), 200
            else:
                return jsonify({'error': 'Token not found in response'}), 500
        else:
            # Manejar errores del microservicio autorizador
            return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Authorization service request failed', 'details': str(e)}), 502
    
@app.route('/incidentes', methods=['POST'])
def consulta_incidentes():
    auth_header = request.headers.get('Authorization')
    if validar_token(auth_header) == True:
        return "Consulta realizada correctamente", 200
    else:
        return validar_token(auth_header)

        
def validar_token(token):
    if not token:
        return jsonify({'error': 'Token are required'}), 400
    try:
        # Enviar el token al microservicio autorizador
        response = requests.post(f"{AUTHORIZER_URL}/validateToken", json=token)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            return True
        else:
            # Manejar errores del microservicio autorizador
            return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Authorization service request failed', 'details': str(e)}), 502


if __name__ == '__main__':
    app.run(port=5000)