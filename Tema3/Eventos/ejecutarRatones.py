from threading import Event

from Eventos.cRatones import Raton

if __name__ == '__main__':

    ratones = 5
    e = Event()
    e.set()

    estudiantes = [Raton(i + 1, e) for i in range(ratones)]

    for e in estudiantes:
        e.start()

    for e in estudiantes:
        e.join()