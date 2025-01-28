import random
from threading import Thread, Semaphore
from time import sleep


class PuenteEstrecho(Thread):

    semaforoN = Semaphore(1)
    semaforoS = Semaphore(1)

    def __init__(self, nombreCoche, direccion):
        Thread.__init__(self)
        self.nombreCoche = nombreCoche
        self.direccion = direccion

    def run(self):

        if self.direccion == 0:

            self.semaforoN.acquire()
            self.semaforoS.acquire()
            print(f"El coche {self.nombreCoche} entró al puente (Norte)")
            sleep(random.randint(1, 5))
            print(f"Ha salido del puente el coche {self.nombreCoche} (Norte)")
            self.semaforoN.release()
            self.semaforoS.release()

        else:

            self.semaforoS.acquire()
            self.semaforoN.acquire()
            print(f"El coche {self.nombreCoche} entró al puente (Sur)")
            sleep(random.randint(1, 5))
            print(f"Ha salido del puente el coche {self.nombreCoche} (Sur)")
            self.semaforoS.release()
            self.semaforoN.release()