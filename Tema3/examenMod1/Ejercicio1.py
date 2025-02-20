import random
from threading import Thread, Semaphore
from time import sleep


class Hamburgueseria(Thread):

    ticket = Semaphore(2)
    dependientes = Semaphore(5)

    def __init__(self, nombre):
        Thread.__init__(self)
        self.nombre = nombre

    def run(self):

        print(f"El cliente {self.nombre} está esperando a sacar el ticekt")
        self.ticket.acquire()
        sleep(random.randint(1, 4))
        print(f"El cliente {self.nombre} ha sacado el ticket")
        self.ticket.release()

        print(f"El cliente {self.nombre} está esperando a ser atendido")
        self.dependientes.acquire()
        sleep(random.randint(3, 7))
        print(f"El cliente {self.nombre} ha sido atendido y se va")
        self.dependientes.release()

if __name__ == "__main__":

    for i in range(10):
        h = Hamburgueseria(i)
        h.start()