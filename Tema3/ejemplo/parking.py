import random
from threading import Thread, Semaphore
from time import sleep

class Aparcamiento(Thread):

    espacios = 5
    semaforo = Semaphore(espacios)

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        self.nombre = nombre

    def run(self):

        self.semaforo.acquire()
        print(f" \U0001F697 Vehículo {self.nombre} está entrando al estacionamiento.")
        self.espacios -= 1
        sleep(random.randint(1, 10))
        self.espacios += 1
        print(f" \U0001F697 Vehículo {self.nombre} salió del estacionamiento. Espacios disponibles: {self.espacios}")
        self.semaforo.release()
