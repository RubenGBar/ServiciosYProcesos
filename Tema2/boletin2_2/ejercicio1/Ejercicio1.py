from multiprocessing import *

def sumaNum(num):
    suma = 0
    for i in range(1, num+1):
        suma += i
    print("Suma de todos los valores hasta el " + str(num) + " : " + str(suma))
    return suma

if __name__ == '__main__':
    res = 0
    n = int(input("¿Hasta que número quieres sumar?\n"))
    numeros = []

    for i in range(1, n+1):
        numeros.append(i)

    with Pool(processes = 3) as pool:
        res = pool.map(sumaNum, numeros)
