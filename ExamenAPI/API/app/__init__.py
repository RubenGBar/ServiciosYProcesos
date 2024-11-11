from flask import Flask
from flask_jwt_extended import JWTManager

from API.app.dispositivos.rutas import dispositivosBP
from API.app.usuarios.rutas import usuariosBP

app = Flask(__name__)
app.register_blueprint(dispositivosBP, url_prefix='/dispositivos')
app.register_blueprint(usuariosBP, url_prefix='/usuarios')

app.config["JWT_SECRET_KEY"] = 'tu_clave'
jwt = JWTManager(app)