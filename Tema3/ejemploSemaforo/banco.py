import random
from mimetypes import init
from threading import Thread, Semaphore
from time import sleep


class Banco(Thread):

    semaforo = Semaphore(3)

    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):
        init()

        self.semaforo.acquire()
        print(f"La persona {self.nombre} entró al cajero")
        sleep(random.randint(1, 5))
        print(f"Ha salido del cajero la persona {self.nombre}")
        self.semaforo.release()
