from flask import Blueprint, jsonify

countriesBP = Blueprint('countries', __name__)

@countriesBP.get('/countries')
def get_countries():
    countries = leeFichero()
    return jsonify(countries)