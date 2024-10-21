import app
from flask import Flask
from .countries.routes import countriesBP
from .cities.routes import citiesBP, rutaFichero
from .ficheros import leeFichero
from flask_jwt_extended import JWTManager
from .users.routes import usersBP

app.config['SECRET_KEY'] = "clave_secreta"
app = Flask(__name__)
app.register_blueprint(countriesBP, url_prefix='/countries')
app.register_blueprint(citiesBP, url_prefix='/cities')
app.register_blueprint(usersBP, url_prefix='/users')
app.config['SECRET_KEY'] = 'tu_clave'
jwt = JWTManager(app)