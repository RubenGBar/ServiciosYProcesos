from multiprocessing import *

def sumaNum(id, num):
    suma = 0
    print("n=",num)
    for i in range(1, num+1):
        suma += i
        print("Proceso: " + str(id) + " Suma de todos los valores hasta el " + str(i) + " : " + str(suma))
    return suma

if __name__ == '__main__':

    with Pool(processes = 3) as pool:
        numbers = [(1, 2), (2, 4), (3, 5), (4, 7), (5, 8)]

        res = pool.starmap(sumaNum, numbers)

    print("Resultados: " + str(res))