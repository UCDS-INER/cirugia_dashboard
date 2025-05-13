from flask import Flask

app = Flask(__name__)

from app import main  # Importar el módulo main para definir las rutas y la lógica de la aplicación.