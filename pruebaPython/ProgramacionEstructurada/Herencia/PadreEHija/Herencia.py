#coding: latin1
class Padre():
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        print("Hola, soy el padre: " + self.nombre)

    def getNombre(self):
        return self.nombre

class Hija(Padre):
    def __init__(self, nombre, padre):
        self.padre=padre
        super().__init__(nombre)

    def saludo(self):
        print("Hola, soy la hija: " + self.nombre + " y mi padre es " + self.padre.getNombre())

padre = Padre("Paco")
hija = Hija("Lucía", padre)

padre.saludo()
hija.saludo()