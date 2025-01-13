import random
import threading
import time
from threading import Thread

class Panaderia(threading.Thread):
    barras = 7
    venta = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)

    def compra_pan(self):
        Panaderia.venta.acquire()
        if (Panaderia.barras > 0):
            Panaderia.barras = Panaderia.barras - 1
            ok = True
        else:
            print("No queda pan")
            ok = False
        Panaderia.venta.release()
        return ok

class Comprador(threading.Thread):
    def __init__(self, nombre, panaderia):
        threading.Thread.__init__(self, name=nombre)
        self.nombre = nombre
        self.tiendaHabitual = panaderia

    def run(self):
        print(f"Soy el hilo {self.nombre} comprando pan")
        time.sleep(random.randint(1, 3))
        if(self.tiendaHabitual.compra_pan()):
            print(f"El hilo {self.nombre} ha comprado pan")
        else:
            print(f"El hilo {self.nombre} no ha comprado pan")