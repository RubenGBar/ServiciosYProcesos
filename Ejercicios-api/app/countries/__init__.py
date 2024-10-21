from flask import Blueprint, jsonify, request

from Ejemplo.EjemploFlask import app
from app import countries
from app.ficheros import leeFichero, escribeFichero

rutaFichero = "app\\ficheros\\countries.json"

@app.get("/countries/<int:id>")
def get_country(id):
    countries = leeFichero("countries.json")
    for country in countries:
        if country['id'] == id:
            return country, 200
    return {"error": "Country not found"}, 404

@app.post("/countries")
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