from mimetypes import init
from threading import Thread, Semaphore
from time import sleep


class SalaCine(Thread):

    espacios = 20
    semaforo = Semaphore(espacios)

    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        init()

        self.semaforo.acquire()
        print(f"Espectador {self.nombre} ha entrado al cine")
        sleep(5)
        print(f"Ha salido del cine el espectador {self.nombre}")
        self.semaforo.release()
