import app
from flask import Flask
from .countries.routes import countriesBP
from .cities.routes import citiesBP, rutaFichero
from .ficheros import leeFichero
app = Flask(__name__)
app.register_blueprint(countriesBP, url_prefix='/countries')
app.register_blueprint(citiesBP, url_prefix='/cities')
