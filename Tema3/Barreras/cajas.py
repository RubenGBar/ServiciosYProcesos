import random
import time
from threading import Thread, Barrier


class Caja(Thread):
    def __init__(self, nombre, barrera: Barrier):
        Thread.__init__(self)
        self.nombre = nombre
        self.barrera = barrera

    def run(self):
        self.barrera.wait()
        resto = self.barrera.wait()
        print(f"Hilo {self.nombre} entra en caja y quedan {resto}\n")
        time.sleep(random.randint(1, 3))
        print(f"Hilo {self.nombre} sale de caja\n")

if __name__ == "__main__":
    barrera = Barrier(5)

    hilos = []

    for i in range(10):
        hilo = Caja(f"{i}", barrera)
        time.sleep(random.randint(1, 3))
        hilo.start()
        hilos.append(hilo)

    for h in hilos:
        h.join()