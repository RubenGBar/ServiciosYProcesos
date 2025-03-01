from multiprocessing import *

def sumaNum(id, num):
    suma = 0
    print("n=",num)
    for i in range(1, num+1):
        suma += i
        print("Proceso: " + str(id) + " Suma de todos los valores hasta el " + str(i) + " : " + str(suma))

if __name__ == '__main__':
    p1 = Process(target=sumaNum, args=(1, 2))
    p2 = Process(target=sumaNum, args=(2, 4))
    p3 = Process(target=sumaNum, args=(3, 5))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()
