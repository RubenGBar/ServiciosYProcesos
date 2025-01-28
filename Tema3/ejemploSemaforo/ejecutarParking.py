from ejemploSemaforo.parking import Aparcamiento

if __name__ == '__main__':

    print("Soy el hilo Principal")
    for i in range(1, 10):
        p = Aparcamiento(i)
        p.start()