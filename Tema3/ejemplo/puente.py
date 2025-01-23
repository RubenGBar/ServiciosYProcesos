import random
from threading import Thread, Semaphore
from time import sleep


class PuenteEstrecho(Thread):

    espacio = 1
    semaforoN = Semaphore(espacio)
    semaforoS = Semaphore(espacio)

    def __init__(self, nombreCoche, direccion):
        Thread.__init__(self)
        self.nombreCoche = nombreCoche
        self.direccion = direccion

    def run(self):

        if self.direccion == 0:

            self.semaforoN.acquire()
            self.semaforoS.acquire()
            self.espacio -= 1
            print(f"El coche {self.nombreCoche} entró al puente Norte")
            sleep(random.randint(1, 5))
            self.espacio += 1
            print(f"Ha salido del puente Norte el coche {self.nombreCoche}")
            self.semaforoN.release()
            self.semaforoS.release()

        else:

            self.semaforoS.acquire()
            self.semaforoN.acquire()
            self.espacio -= 1
            print(f"El coche {self.nombreCoche} entró al puente Sur")
            sleep(random.randint(1, 5))
            self.espacio += 1
            print(f"Ha salido del puente Sur el coche {self.nombreCoche}")
            self.semaforoS.release()
            self.semaforoN.release()