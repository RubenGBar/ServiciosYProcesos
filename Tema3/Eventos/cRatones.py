import random
import time
from threading import Thread, Event


class Raton(Thread):

    def __init__(self, nombre, event:Event):
        Thread.__init__(self)
        self.evento = event
        self.nombre = nombre

    def run(self):

        while not self.evento.is_set():
            self.evento.wait()
        self.evento.clear()
        print(f"El ratón {self.nombre} tomó el control del plato")
        time.sleep(random.randint(1, 3))
        print(f"El ratón {self.nombre} terminó de comer")
        self.evento.set()