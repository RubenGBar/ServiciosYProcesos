from mercados import Supermercado

if __name__ == '__main__':

    print("Soy el hilo Principal")
    for i in range(1, 10):
        m = Supermercado(i)
        m.start()