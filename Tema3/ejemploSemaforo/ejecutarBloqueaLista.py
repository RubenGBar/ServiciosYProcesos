from bloquearLista import BloqueaLista

if __name__ == '__main__':
    print("Soy el hilo principal")
    for i in range(15):
        h = BloqueaLista("Hilo" + str(i))
        h.start()