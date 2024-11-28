from multiprocessing import Process, Queue

def leerFichero(cola: Queue):
    with open("numeros.txt", "r") as archivo:
        for linea in archivo.readlines():
            num = int(linea)
            cola.put(num)
            print("Añadiendo " + str(num))
        cola.put(None)

def sumaNumeros(cola: Queue):

    suma = 0
    numeros = cola.get()
    while numeros is not None:
        for i in range(1, numeros + 1):
            suma += i
        print("Suma hasta " + str(numeros) + " : " + str(suma))
        numeros = cola.get()
    return suma

if __name__ == '__main__':

    cola = Queue()
    p1 = Process(target=leerFichero, args=(cola,))
    p2 = Process(target=sumaNumeros, args=(cola,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()