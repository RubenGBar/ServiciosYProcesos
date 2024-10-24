from flask import Blueprint, jsonify, request

from app import app, cities
from app.ficheros import leeFichero, escribeFichero

rutaFichero = "Ejercicios-api/app/ficheros/cities.json"
citiesBP = Blueprint('cities', __name__)

@citiesBP.get('/')
def get_cities():
    cities = leeFichero("cities.json")
    return jsonify(cities)

@citiesBP.get("/<int:id>")
def get_city(id):
    cities = leeFichero("cities.json")
    for city in cities:
        if city["id"] == id:
            return city, 200
    return {"error": "Country not found"}, 404

@citiesBP.get("/<int:id>/cities")
def get_cities(id):
    list = []
    cities = leeFichero("cities.json")
    for city in cities:
        if city["countryId"] == id:
            list.append(city)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No cities for this country"}, 404

@citiesBP.post('/')
def add_city():
    cities = leeFichero("cities.json")

    if request.is_json:
        city = request.get_json()
        city["id"] = find_next_id()
        cities.append(city)
        escribeFichero(cities, "cities.json")
        return city, 201

    return {"error": "Request must be json"}, 415

def find_next_id():
    return max(country["id"] for country in cities) + 1