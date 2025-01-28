from ejemploCondition.pruebaCondition import Lista

if __name__ == '__main__':

    print("Soy el hilo Principal")
    for i in range(1, 10):
        p = Lista(i)
        p.start()