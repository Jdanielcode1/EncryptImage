from flask import Flask, request, send_file
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    decrypted_image_path = 'decrypted_image.jpg'
    
    # Verificar si existe una imagen desencriptada
    if os.path.exists(decrypted_image_path):
        # Enviar la imagen desencriptada como respuesta
        return send_file(decrypted_image_path, mimetype='image/jpeg')
    else:
        return 'No hay imagen desencriptada disponible.'

@app.route('/decrypt', methods=['POST'])
def decrypt_image():
    # Obtener los datos encriptados de la imagen y la clave de la solicitud
    encrypted_data = request.files['image'].read()
    key = request.form.get('key')

    if key:
        # Crear una instancia de Fernet con la clave y desencriptar los datos
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        # Guardar la imagen desencriptada en el servidor
        decrypted_image_path = 'decrypted_image.jpg'
        with open(decrypted_image_path, 'wb') as file:
            file.write(decrypted_data)

        return 'Imagen desencriptada y disponible en la URL raíz.'
    else:
        return 'Clave de desencriptado no proporcionada.'

if __name__ == '__main__':
    app.run()