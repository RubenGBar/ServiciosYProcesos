#coding: latin1
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if(self.num2 == 0):
            print("No se puede hacer la divisi�n")
        return self.num1 / self.num2

class main():

    num1 = input("Introduzca un n�mero\n")
    num2 = input("Introduzca otro n�mero\n")

    cal = Calculadora(int(num1), int(num2))

    print()
    print("Suma: " + str(cal.sumar()))
    print("Resta: " + str(cal.restar()))
    print("Multiplicaci�n: " + str(cal.multiplicar()))
    print("Divisi�n: " + str(cal.dividir()))

if __name__ == "__main__":
    main()