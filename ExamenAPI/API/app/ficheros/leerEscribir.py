import json

# funcion para leer el fichero de dispositivos
def leerFichero(ruta):
    archivo = open(ruta, "r")
    objeto = json.load(archivo)
    archivo.close()
    return objeto

# funcion para escribir el fichero de dispositivos
def escribirFichero(ruta, objeto):
    archivo = open(ruta, "w")
    json.dump(objeto, archivo)
    archivo.close()