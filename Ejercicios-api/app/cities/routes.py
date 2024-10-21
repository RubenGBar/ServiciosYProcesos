from flask import Blueprint, jsonify

from app.ficheros import leeFichero

rutaFichero = "app\\ficheros\\cities.json"
citiesBP = Blueprint('cities', __name__)

@citiesBP.get('/')
def get_cities():
    cities = leeFichero("cities.json")
    return jsonify(cities)

@citiesBP.post('/<int:id>')
def get_city(id):
    cities = leeFichero("cities.json")
    for city in cities:
        if city['id'] == id:
            return city, 200
    return {"error": "Country not found"}, 404

@citiesBP.post('/<int:id>/cities')
def get_cities(id):
    list = []
    cities = leeFichero("cities.json")
    for city in cities:
        if city['countryId'] == id:
            list.append(city)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No cities for this country"}, 404