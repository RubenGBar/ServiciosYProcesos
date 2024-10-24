from flask import Blueprint, jsonify, request

from app import countries, app
from app.ficheros import leeFichero, escribeFichero

countriesBP = Blueprint('contries', __name__)
rutaFichero = "Ejercicios-api/app/ficheros/countries.json"
rutaCities="Ejercicios-api/app/ficheros/cities.json"
@countriesBP.get('/')
def get_countries():
    countries = leeFichero("countries.json")
    return jsonify(countries)

@countriesBP.post("/<int:id>")
def get_country(id):
    countries = leeFichero("countries.json")
    for country in countries:
        if country["id"] == id:
            return country, 200
    return {"error": "Country not found"}, 404

@countriesBP.get("/<int:id>/cities")
def get_countries_cities(id):
    list = []
    cities = leeFichero(rutaCities)
    for city in cities:
        if city['idCountry'] == id:
            list.append(city)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No hay cities para esa country"}, 404

@countriesBP.post('/')
def add_country():
    countries = leeFichero("countries.json")

    if request.is_json:
        country = request.get_json()
        country["id"] = find_next_id()
        countries.append(country)
        escribeFichero(countries, "countries.json")
        return country, 201

    return {"error": "Request must be json"}, 415

def find_next_id():
    return max(country["id"] for country in countries) + 1