from flask import Blueprint, jsonify

from app.ficheros import leeFichero

countriesBP = Blueprint('contries', __name__)

@countriesBP.get('/')
def get_countries():
    countries = leeFichero("country.json")
    return jsonify(countries)

@countriesBP.post('/<int:id>')
def get_country(id):
    countries = leeFichero("country.json")
    for country in countries:
        if country["id"] == id:
            return country, 200
    return {"error": "Country not found"}, 404

@countriesBP.post('/<int:id>/countries')
def get_countries(id):
    list = []
    countries = leeFichero("country.json")
    for country in countries:
        if country["id"] == id:
            return country, 200
    return {"error": "Country not found"}, 404