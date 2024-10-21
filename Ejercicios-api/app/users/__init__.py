import bcrypt
from flask import request
from flask_jwt_extended import create_access_token

from app import leeFichero
from app.ficheros import escribeFichero


def registerUser():
    users = leeFichero("users.json")
    if request.is_json:
        user = request.get_json()
        password = user["password"].encode('utf-8')

        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(password, salt).hex()

        user['password'] = hashPassword
        users.append(user)
        escribeFichero(users, "users.json")

        token = create_access_token(identity=user['username'])
        return {'token': token}, 201
    
    return {"error:", "Request must be JSON"}, 415