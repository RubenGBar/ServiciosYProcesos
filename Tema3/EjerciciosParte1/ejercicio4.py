from threading import Thread, Lock


class Texto(Thread):

    bloqueo = Lock()
    texto = "Llev"

    def __init__(self):
        Thread.__init__(self)