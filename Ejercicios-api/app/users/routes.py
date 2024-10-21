from flask import Blueprint, request

ficheroUsers = "../app/ficheros/users.json"

usersBP = Blueprint('usersBP', __name__)