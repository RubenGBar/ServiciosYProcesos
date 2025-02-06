from threading import Timer


def funcion():
    print("Hola Mundo")

if __name__ == "__main__":
    temporizador = Timer(5, funcion)
    temporizador.start()
    print("Esperando a que se ejecute la función")