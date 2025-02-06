import random
from threading import Thread
from time import sleep


class Persona(Thread):

    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre
        self.contador = 0

    def run(self):

        while True:
            self.contador += 1
            print(f"Soy {self.nombre} y estoy trabajando")
            sleep(random.randint(1,10))
            print(f"Soy {self.nombre} y he terminado de trabajar. Llevo {self.contador} horas trabajadas")

if __name__ == '__main__':

    for i in range(5):
        p = Persona(f"Persona {i+1}")
        p.start()