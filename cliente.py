import requests
from cryptography.fernet import Fernet

def encrypt_image(image_path, key):
    # Leer los datos de la imagen
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Crear una instancia de Fernet con la clave y encriptar los datos de la imagen
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(image_data)

    return encrypted_data

def send_encrypted_image(encrypted_data, key):
    # URL del servidor para la ruta de desencriptado
    url = 'http://localhost:5000/decrypt'
    
    # Crear los datos de la solicitud con la imagen encriptada y la clave
    files = {'image': ('encrypted_image.bin', encrypted_data)}
    data = {'key': key}
    
    # Enviar la solicitud POST al servidor con los datos
    response = requests.post(url, files=files, data=data)
    
    return response.text

# Ejemplo de uso
image_path = 'imagen.jpg'
key = Fernet.generate_key()
encrypted_data = encrypt_image(image_path, key)
result = send_encrypted_image(encrypted_data, key)
print(result)