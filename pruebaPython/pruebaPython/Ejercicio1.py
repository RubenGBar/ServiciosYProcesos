#coding: latin1
def mostarNumeros(num1, num2):

    numeroMayor = num2 if (num2 > num1) else num1

    for contador in range(int(num1), int(num2)):
        print(contador, end=", ")

def main():

    num1 = input("Dime un n�mero\n")
    num2 = input("Dime un n�mero mayor\n")

    mostarNumeros(num1, num2)

if __name__ == "__main__":
    main()