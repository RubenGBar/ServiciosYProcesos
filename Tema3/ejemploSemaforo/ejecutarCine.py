from time import sleep

from ejemploSemaforo.cine import SalaCine

if __name__ == '__main__':

    print("Soy el hilo Principal")
    for i in range(1, 30):
        p = SalaCine(i)
        p.start()
        sleep(5)