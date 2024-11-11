import bcrypt
from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from API.app.ficheros.leerEscribir import leerFichero, escribirFichero

ficheroUsuarios = "app/usuarios/usuarios.json"
usuariosBP = Blueprint('usuarios', __name__)

# funcion que registra a los usuarios para que puedan utilizar los metodos protegiods por tokens
@usuariosBP.post('/')
def registro_Usuario():
    usuarios = leerFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.json
        contrasenia = usuario['contrasenia'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashContrasenia = bcrypt.hashpw(contrasenia, salt).hex()
        usuario['contrasenia'] = hashContrasenia
        usuarios.append(usuario)
        escribirFichero(ficheroUsuarios, usuarios)
        token = create_access_token(identity=usuario["usuario"])
        return {'token': token}, 201
    return {"error": "Request must be JSON"}, 415

# funcion que realiza el login del usuario comprobando antes si existe
def login_Usuario():
    usuarios = leerFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.json
        nombreUsuario = usuario['usuario']
        contraseniaUsuario = usuario['contrasenia'].encode('utf-8')
        for archivoUsuario in usuarios:
            if archivoUsuario['usuario'] == nombreUsuario:
                archivoContrasenia = archivoUsuario['contrasenia']
                if bcrypt.checkpw(contraseniaUsuario, bytes.fromhex(archivoContrasenia)):
                    token = create_access_token(identity=nombreUsuario)
                    return {'token': token}, 200
                else:
                    return {'error': 'Not authorized'}, 401
        return {'error': 'User not found'}, 401
    return {"error": "Request must be JSON"}, 415