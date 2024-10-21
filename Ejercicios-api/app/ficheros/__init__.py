import json

def leeFichero(ruta):
    archivo = open(ruta, "r")
    countries = json.load(archivo)
    archivo.close()
    return countries

def escribeFichero(countries, ruta):
    archivo = open(ruta, "w")
    json.dump(countries, archivo)
    archivo.close()
