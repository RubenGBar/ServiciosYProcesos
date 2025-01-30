import random
import time
from threading import Thread, Condition

class Biblioteca(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.libros = [False, False, False, False, False, False, False, False, False]
        self.cond = Condition()

class Estudiante(Thread):

    def __init__(self, nombre, biblioteca):
        Thread.__init__(self)
        self.name = nombre
        self.biblio = biblioteca
        self.libro1 = random.randint(0, 8)
        self.libro2 = random.randint(0, 8)
        while self.libro1 == self.libro2:
            self.libro2 = random.randint(0, 8)

    def run(self):

        with self.biblio.cond:
            while (self.biblio.libros[self.libro1] == True or self.biblio.libros[self.libro2] == True):
                print(f"El alumno {self.name} está esperando a que el libro {self.libro1} y {self.libro2} estén libres")
                self.biblio.cond.wait()

            self.biblio.libros[self.libro1] = True
            self.biblio.libros[self.libro2] = True

        print(f"El alumno {self.name} está usando el libro {self.libro1} y {self.libro2}")
        time.sleep(random.randint(3, 5))
        print(f"El alumno {self.name} ha terminado de usar el libro {self.libro1} y {self.libro2}")

        with self.biblio.cond:
            self.biblio.libros[self.libro1] = False
            self.biblio.libros[self.libro2] = False
            self.biblio.cond.notify_all()
