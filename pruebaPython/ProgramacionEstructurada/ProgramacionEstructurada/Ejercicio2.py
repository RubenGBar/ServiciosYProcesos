#coding: latin1
def main():

    num1 = input("Dime un n�mero\n")
    
    num2 = input("Dime otro n�mero\n")

    if int(num1)>int(num2):
        print("El n�mero " + str(num1) + " es mayor que el n�mero " + str(num2))
    else:
        print("El n�mero " + str(num2) + " es mayor que el n�mero " + str(num1))

if __name__ == "__main__":
    main()
