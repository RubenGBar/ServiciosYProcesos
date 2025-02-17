import random
from threading import Thread, Condition
from time import sleep


class Mesa(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.palillos = [True, True, True, True, True]
        self.cond = Condition()

class Filosofo(Thread):

    def __init__(self, nombre, mesa: Mesa):
        Thread.__init__(self)
        self.nombre = nombre
        self.mesa = mesa

        # Evito el bloqueo haciendo que el último tome sus palillos en orden inverso al de los demás
        if nombre == 4:
            self.palillo1 = (nombre + 1) % 5
            self.palillo2 = nombre
        else:
            self.palillo1 = nombre
            self.palillo2 = (nombre + 1) % 5

    def run(self):
        while True:
            sleep(random.randint(3, 7))

            with self.mesa.cond:
                while not self.mesa.palillos[self.palillo1]:
                    print(f"El filósofo {self.nombre} está esperando por el palillo izquierdo {self.palillo1}")
                    self.mesa.cond.wait()

                self.mesa.palillos[self.palillo1] = False

                while not self.mesa.palillos[self.palillo2]:
                    print(f"El filósofo {self.nombre} está esperando por el palillo derecho {self.palillo2}")
                    self.mesa.cond.wait()

                self.mesa.palillos[self.palillo2] = False

            print(f"El filósofo {self.nombre} está comiendo con los palillos {self.palillo1} y {self.palillo2}")
            sleep(random.randint(3, 7))

            with self.mesa.cond:
                self.mesa.palillos[self.palillo1] = True
                self.mesa.palillos[self.palillo2] = True
                print(f"El filósofo {self.nombre} ha devuelto los palillos {self.palillo1} y {self.palillo2}")
                self.mesa.cond.notify_all()

if __name__ == "__main__":

    mesa = Mesa()

    for i in range(5):
        f = Filosofo(i, mesa)
        f.start()