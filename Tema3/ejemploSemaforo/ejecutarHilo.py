from nuevoEjemploHilos import MiHilo

print("Soy el hilo principal")

for i in range (0,10):
    t = MiHilo(i)
    t.start()