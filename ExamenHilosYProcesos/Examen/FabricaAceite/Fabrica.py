import random
from threading import Thread, Condition
from time import sleep

class Tolva(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.capacidad = 0

class Operario(Thread):

    def __init__(self, nombre, tolva: Tolva):
        Thread.__init__(self)
        self.nombre = nombre
        self.tolva = tolva
        self.bloqueo = Condition()

    def run(self):

        while True:
            with (self.bloqueo):
                while self.tolva.capacidad >= 500:
                    print(f"El operario {self.nombre} está esperando a llenar la tolva")
                    self.bloqueo.wait()

                rellenar = random.randint(5, 30)

                while rellenar + self.tolva.capacidad > 500:
                    rellenar = random.randint(5, 30)


                print(f"Rellenando la tolva con {rellenar} litros")
                self.tolva.capacidad += rellenar
                sleep(random.randint(1, 5))

                print(f"Capacidad: {self.tolva.capacidad}")

                self.bloqueo.notify_all()

class Embotellar(Thread):

    def __init__(self, nombre, tolva: Tolva):
        Thread.__init__(self)
        self.nombre = nombre
        self.tolva = tolva
        self.bloqueo = Condition()

    def run(self):

        while True:
            with (self.bloqueo):
                while self.tolva.capacidad <= 4:
                    print(f"La línea de embotellado {self.nombre} está esperando a poder sacar aceite")
                    self.bloqueo.wait()

                print(f"Embotellando aceite")
                self.tolva.capacidad -= 5
                sleep(random.randint(1, 2))

                print(f"Capacidad: {self.tolva.capacidad}")

                self.bloqueo.notify_all()

if __name__ == "__main__":

    # He usado una condicion como metodo de sincronización ya que creo que es el más adecuado cuando varios procesos intentar acceder al mismo recuros y manipularlo de maneras distintas

    tolva = Tolva()
    # Ejecución constante: Operarios = 4 y Lineas = 2
    # Operarios esperando: Operarios = 50 y Lineas = 1
    # Lineas esperando: Operarios = 2 y Lineas = 50
    numOperarios = 4
    numLineas = 2

    operarios = [Operario(i, tolva) for i in range(numOperarios)]
    lineas = [Embotellar(i, tolva) for i in range(numLineas)]

    for operario in operarios:
        operario.start()

    for linea in lineas:
        linea.start()

    for operario in operarios:
        operario.join()

    for linea in lineas:
        linea.join()