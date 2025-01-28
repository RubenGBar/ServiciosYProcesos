import random
import time
from threading import Thread, Condition

class Panaderia(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.barras = 7
        self.venta = Condition()

class Reponedor(Thread):

    def __init__(self, panaderia):
        Thread.__init__(self)
        self.p = panaderia

    def run(self):

        while True:
            with self.p.venta:
                while self.p.barras > 0:
                    self.p.venta.wait()
                print(f"Reponiendo panes")
                time.sleep(random.uniform(0.1, 0.5))
                self.p.barras = 7
                print(f"Panes a la venta")
                self.p.venta.notify_all()

class Comprador(Thread):

    def __init__(self, nombre, panaderia):
        Thread.__init__(self, name=nombre)
        self.nombre = nombre
        self.p = panaderia

    def run(self):

        with self.p.venta:
            while self.p.barras == 0:
                print(f"El comprador {self.name} está esperando a que haya pan")
                self.p.venta.wait()

            print(f"El comprador {self.name} ha comprado pan. Quedan {self.p.barras}")
            self.p.barras -= 1
            time.sleep(random.uniform(0.1, 0.5))
            self.p.venta.notify_all()