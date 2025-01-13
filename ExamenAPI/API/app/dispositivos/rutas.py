from flask import jsonify, Blueprint, request
from flask_jwt_extended import jwt_required

from API.app.ficheros.leerEscribir import leerFichero, escribirFichero

ruta = "app/ficheros/devices.json"

dispositivosBP = Blueprint('dispositivos', __name__)

# funcion para obtener todos los dispositivos
@dispositivosBP.get('/')
def get_dispositivos():
    dispositivos = leerFichero(ruta)
    return jsonify(dispositivos)

# funcion para añadir los dispositivos protegida con auteticación por token
@dispositivosBP.post('/')
@jwt_required
def add_dispositivos():
    dispositivos = leerFichero(ruta)
    if request.is_json:
        if dispositivos['id'].isdigit() and dispositivos['name'].isalpha() and (dispositivos['tipo'].equals("luz") or dispositivos['tipo'].equals("termostato")):
            dispositivos = request.get_json()
            dispositivos['id'] = findNextId()
            dispositivos.append(dispositivos)
            escribirFichero(ruta, dispositivos)
            return dispositivos, 201
    return{"error": "Request must be json"}, 415

# funcion para actulizar los dispositivos protegida con autenticación por token
@dispositivosBP.put("/<int:id>")
@dispositivosBP.patch("/<int:id>")
@jwt_required
def update_dispositivos(id):
    if request.is_json:
        dispositivos = leerFichero(ruta)
        nuevoDispositivo = request.get_json()

        for dispositivo in dispositivos:
            if dispositivo["id"] == id:
                if dispositivo["tipo"].equals("luz"):
                    for elemento in nuevoDispositivo:
                        dispositivo[elemento] = nuevoDispositivo[elemento]
                        escribirFichero(ruta, dispositivo)
                        return dispositivo, 200
                elif dispositivo["tipo"].equals("termostato"):
                    for elemento in nuevoDispositivo:
                        dispositivo[elemento] = nuevoDispositivo[elemento]
                        escribirFichero(ruta, dispositivo)
                        return dispositivo, 200

    return{"error": "Request must be json"}, 415

# funcion para eliminar los dispositivos protegida con autenticación por token
@dispositivosBP.delete("/<int:id>")
@jwt_required
def delete_dispositivos(id):
    dispositivos = leerFichero(ruta)
    for dispositivo in dispositivos:
        if dispositivo["id"] == id:
            dispositivos.remove(dispositivo)
            escribirFichero(ruta, dispositivo)
            return "{}", 200
    return {"error": "Dispositivo not found"}, 404

def findNextId():
    dispositivos = leerFichero(ruta)
    return max(dispositivo["Id"] for dispositivo in dispositivos) + 1