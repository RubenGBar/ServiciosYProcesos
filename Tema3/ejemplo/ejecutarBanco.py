from ejemplo.banco import Banco

if __name__ == '__main__':

    print("Soy el hilo Principal")
    for i in range(1, 10):
        b = Banco(i)
        b.start()