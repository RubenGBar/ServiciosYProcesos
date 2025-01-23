import random

from ejemplo.puente import PuenteEstrecho

if __name__ == '__main__':

    print("Soy el hilo Principal")
    for i in range(1, 10):
        p = PuenteEstrecho(i, random.randint(0,1))
        p.start()