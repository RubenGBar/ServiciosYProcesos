from flask import Blueprint, jsonify, request

from Ejemplo.EjemploFlask import app
from app import cities
from app.ficheros import leeFichero, escribeFichero

rutaFichero = "app\\ficheros\\cities.json"

@app.get("/cities/<int:id>")
def get_city(id):
    cities = leeFichero("cities.json")
    for city in cities:
        if city["id"] == id:
            return city, 200
    return {"error": "Country not found"}, 404

@app.post("/cities")
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