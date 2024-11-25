from multiprocessing import *


def incrementar(id, valor, lock):

    for _ in range(10):
        with lock:
            print(f"P{id} incrementa el valor {valor.value}")
            valor.value += 1

if __name__ == '__main__':
    contador = Value('i', 0)
    numProcesos = 4
    lock = Lock()
    procesos = []
    for i in range(numProcesos):
        p = Process(target=incrementar, args=(i, contador, lock,))
        procesos.append(p)
    for p in procesos:
        p.start()
    for p in procesos:
        p.join()
    print(f"Valor final del contador: {contador.value}")