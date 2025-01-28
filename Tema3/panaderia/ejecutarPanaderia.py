from panaderia.cPanaderia import Comprador, Panaderia, Reponedor

if __name__ == '__main__':

    numCompradores = 105
    p = Panaderia()
    reponedor = Reponedor(p)
    compradores = [Comprador(i, p) for i in range(numCompradores)]

    for c in compradores:
        c.start()
    reponedor.start()

    for c in compradores:
        c.join()
    reponedor.join()
