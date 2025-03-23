import random
from asyncio import Event
from threading import Thread


class Atomos(Thread):

    def __init__(self, atomosListos: Event()):
        Thread.__init__(self)
        self.hidrogeno = 0
        self.oxigeno = 0
        self.atomosListos = atomosListos

    def run(self):

        while True:
            if self.hidrogeno == 1:
                self.hidrogeno += 1
                print("Átomo de Hidrógeno generado")
                self.atomosListos.set()

            elif self.oxigeno == 0:
                self.oxigeno += 1
                print("Átomo de Oxígeno generado")
                self.atomosListos.set()

            else:
                atomoAGenerar = random.randint(0, 1)

                if atomoAGenerar == 0:
                    self.hidrogeno += 1
                elif atomoAGenerar == 1:
                    self.oxigeno += 1

                print("Átomo generado")
                self.atomosListos.set()

class Operario(Thread):

    def __init__(self, nombre, atomos: Atomos, atomosListos: Event()):
        Thread.__init__(self)
        self.nombre = nombre
        self.atomosListos = atomosListos
        self.atomos = atomos

    def run(self):

        while True:

            while not self.atomosListos.is_set():
                print(f"Operario {self.nombre} esperando a que haya suficientes átomos")
                self.atomosListos.wait()

            if self.atomos.oxigeno >= 1 and self.atomos.hidrogeno >= 2:
                self.atomosListos.clear()
                print(f"Operario {self.nombre} está haciendo agua")
                self.atomos.hidrogeno -= 2
                self.atomos.oxigeno -= 1
                self.atomosListos.set()

if __name__ == "__main__":

    # He usado un evento porque así cuando tengo los átomos adecuados para generar el agua se lo notifico a todos los hilos mediante el evento
    atomosListos = Event()
    atomos = Atomos(atomosListos)
    atomos.start()

    for i in range (5):
        o = Operario(i, atomos, atomosListos)
        o.start()