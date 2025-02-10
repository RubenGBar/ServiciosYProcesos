import random
from threading import Thread, Lock, Condition, Barrier


class NumeroAAdivinar(Thread):

    num = random.randint(1, 100)
    cond = Condition()
    barrera = Barrier(5)
    encontrado = False

    def __init__(self):
        Thread.__init__(self)

class adivinarNumero(Thread):

    numeroAdivinar = 0

    def __init__(self, nombre, numero):
        Thread.__init__(self)
        self.nombre = nombre
        self.numero = numero

    def run(self):
        while True:

            try:
                self.numero.barrier.wait()
            except:
                pass

            with self.numero.cond:
                if self.numero.encontrado:
                    break
                else:
                    numeroAleatorio = random.randint(1, 100)
                    if self.numero.num == numeroAleatorio:
                        print(f"El hilo {self.nombre} adivinó el número con: {numeroAleatorio}")
                    else:
                        print(f"El hilo {self.nombre} no adivinó el número con: {numeroAleatorio}")

if __name__ == "__main__":

    numero = NumeroAAdivinar()

    for i in range(1):
        a = adivinarNumero(i, numero)
        a.start()