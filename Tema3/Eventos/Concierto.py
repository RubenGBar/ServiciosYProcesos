import random
import time
from threading import Thread, Event

class Empresa(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.oferta = Event()
        self.ventanilla = Event()
        self.num = 0

    def numTicket(self):
        self.num += 1
        return self.num

    def run(self):
        self.oferta.set()
        self.ventanilla.set()
        print("La oferta ha empezado")
        time.sleep(5)
        print(f"La oferta ha acabado")
        self.oferta.clear()
        self.ventanilla.clear()


class Comprador(Thread):

    def __init__(self, nombre, empresa: Empresa):
        Thread.__init__(self)
        self.nombre = nombre
        self.empresa = empresa

    def run(self):
        compra = True

        while (not self.empresa.oferta.is_set() or not self.empresa.ventanilla.is_set()) and compra:
            compra = self.empresa.oferta.wait(timeout=5)

        if compra:
            self.empresa.oferta.clear()
            print(f"El comprador {self.nombre} está comprando su entrada")
            time.sleep(random.randint(1, 2))
            self.num = self.empresa.numTicket()
            print(f"El comprador {self.nombre} terminó de comprar su entrada con el número {self.num}")
            if self.empresa.oferta.is_set():
                self.empresa.ventanilla.set()
        else:
            print(f"El comprador {self.nombre} no ha podido comprar su entrada")

if __name__ == '__main__':

    empresa = Empresa()
    empresa.start()

    for i in range(5):

        comprador = Comprador(f"{i+1}", empresa)
        comprador.start()

