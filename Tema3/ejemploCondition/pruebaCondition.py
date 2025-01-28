import random
import time
from threading import Thread, Condition


class Lista(Thread):

    lista = [False, False, False, False, False]
    cond = Condition()

    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)

    def run(self):

        num = random.randint(0, 4)

        Lista.cond.acquire()
        while (Lista.lista[num] == True):
            print(f"El hilo {self.name}, está esperando a que se libere la posición, {num}")
            Lista.cond.wait()

        Lista.lista[num] = True
        Lista.cond.release()

        print(f"El hilo {self.name} está usando el objeto {num}")
        time.sleep(random.randint(1, 10))
        print(f"El hilo {self.name} ha terminado de usar el objeto {num}")

        Lista.cond.acquire()
        Lista.lista[num] = False
        Lista.cond.notify_all()
        Lista.cond.release()