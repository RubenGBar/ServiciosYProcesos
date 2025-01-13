import random
from threading import Semaphore,Thread
import time

class Supermercado(Thread):
    semaforo = Semaphore(4)

    def __init__(self, nombre):
        Thread.__init__(self, name = nombre)

    def run(self):
        print(f"Hilo {self.name} va a una caja")
        Supermercado.semaforo.acquire()
        print(f"Hilo {self.name} está siendo atendido")
        time.sleep(random.randint(1,10))
        print(f"Hilo {self.name} está pagando")
        Supermercado.semaforo.release()
        print(f"Hilo {self.name} abandona el supermercado")