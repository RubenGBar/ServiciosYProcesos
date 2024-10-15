#coding: latin1
a = "Hola me llamo pepe"
palabras = a.split()
listas = " ".join(["H", "o", "l", "a"])
print("¡Hola mundo!")
edad=int(input("Dime tu edad\n"))
print("Tienes "+str(edad)+" anos y el doble es "+str((edad*2)))
print("""Texto
         en
         triples
         comillas""")
print(a*2)
print(a[3:10])
print(palabras)
print(listas)

cadena = input("Introduzca una cadena: ")
for letra in cadena:
    print(letra, end=" ")