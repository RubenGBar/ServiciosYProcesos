from multiprocessing import Process, Pipe
from random import randint
from time import sleep

# No sé como hacer que elija un pedido aleatorio y que lo haga solo 50 veces
def telefono(izq1: Pipe):
    fichero = "bocadillos.txt"
    with open(fichero, "r") as f:
        for line in f.readlines():
            pedido = line.strip()
            izq1.send(pedido)
        izq1.send(None)

def cocina(der1: Pipe, izq2: Pipe):
    pedidos = der1.recv()
    while pedidos is not None:
        espera = int(pedidos.split(":")[1].strip())

        sleep(espera)
        izq2.send(pedidos)

        pedidos = der1.recv()
    izq2.send(None)

def reparto(der2: Pipe, id):
    with open("repartos.txt", "w", encoding="utf-8") as f:
        repartir = der2.recv()
        while repartir is not None:
            espera = randint(3, 7)
            bocata = repartir.split(":")[0].strip()

            sleep(espera)
            print(f"Repartidor {id}: Realiza reparto del bocata {bocata}\n")
            # No llega a escibir todos los repartos en el fichero y se queda en un bucle infinito no sé porque :)
            f.write("Repartidor" + str(id) + ": Realiza reparto del bocata " + str(bocata) + "\n")

            repartir = der2.recv()
        der2.send(None)

if __name__ == '__main__':
    izq1, der1 = Pipe()
    izq2, der2 = Pipe()

    teleoperador = Process(target=telefono, args=(izq1,))
    cocinero1 = Process(target=cocina, args=(der1, izq2))
    cocinero2 = Process(target=cocina, args=(der1, izq2))
    repartidor1 = Process(target=reparto, args=(der2, 1))
    repartidor2 = Process(target=reparto, args=(der2, 2))
    repartidor3 = Process(target=reparto, args=(der2, 3))
    repartidor4 = Process(target=reparto, args=(der2, 4))

    teleoperador.start()
    cocinero1.start()
    cocinero2.start()
    repartidor1.start()
    repartidor2.start()
    repartidor3.start()
    repartidor4.start()

    teleoperador.join()
    cocinero1.join()
    cocinero2.join()
    repartidor1.join()
    repartidor2.join()
    repartidor3.join()
    repartidor4.join()

    print("Bocadillos repartidos")