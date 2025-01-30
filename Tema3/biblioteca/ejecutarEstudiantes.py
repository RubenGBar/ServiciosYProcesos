from biblioteca.estudiantes import Biblioteca, Estudiante

if __name__ == '__main__':

    numAlumnos = 4
    b = Biblioteca()
    estudiantes = [Estudiante(i+1, b) for i in range(numAlumnos) ]

    for e in estudiantes:
        e.start()

    for e in estudiantes:
        e.join()