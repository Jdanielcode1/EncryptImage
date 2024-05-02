# EncryptImage
La aplicación descrita es un sistema cliente-servidor diseñado para la transmisión segura de imágenes entre un cliente y un servidor mediante encriptación y desencriptación.

Este programa permite encriptar una imagen en el lado del cliente y enviarla a un servidor para su desencriptación. El servidor desencripta la imagen y la muestra en la URL raíz.

## Requisitos

- Python 3.x
- Bibliotecas: Flask, cryptography, requests

## Instalación

1. Clona este repositorio en tu máquina local.

2. Instala Python:
   - En Windows:
     - Descarga el instalador de Python desde la página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
     - Ejecuta el instalador y sigue las instrucciones. Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
   - En macOS:
     - Abre la terminal y ejecuta el siguiente comando para instalar Python utilizando Homebrew:
       ```
       brew install python
       ```
   - En Linux:
     - Python suele venir preinstalado en la mayoría de las distribuciones de Linux. Si no lo tienes instalado, puedes instalarlo utilizando el administrador de paquetes de tu distribución. Por ejemplo, en Ubuntu, puedes ejecutar el siguiente comando:
       ```
       sudo apt-get install python3
       ```

3. Instala las bibliotecas necesarias ejecutando el siguiente comando:
```
pip3 install flask cryptography requests

```

## Uso

1. Coloca la imagen que deseas encriptar en el mismo directorio que el archivo `cliente.py`. Asegúrate de que la imagen tenga el nombre `imagen.jpg`.

2. Ejecuta el servidor con el siguiente comando:

```
python3 servidor.py
```

3. En otra terminal, ejecuta el cliente con el siguiente comando:
```
python3 cliente.py
```

4. El cliente encriptará la imagen y la enviará al servidor. El servidor desencriptará la imagen y la guardará como `decrypted_image.jpg`.

5. Abre un navegador web y ve a la URL `http://localhost:5000`. Verás la imagen desencriptada mostrada en el navegador.

## Funcionamiento

- El cliente (`cliente.py`) lee los datos de la imagen, genera una clave de encriptación y encripta los datos utilizando la biblioteca `cryptography.fernet`. Luego, envía la imagen encriptada y la clave al servidor a través de una solicitud POST.

- El servidor (`servidor.py`) recibe la imagen encriptada y la clave. Utiliza la clave para desencriptar los datos de la imagen y guarda la imagen desencriptada en el servidor con el nombre `decrypted_image.jpg`. Luego, muestra la imagen desencriptada en la URL raíz (`http://localhost:5000`).




