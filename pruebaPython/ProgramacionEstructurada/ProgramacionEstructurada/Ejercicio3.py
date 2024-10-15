#coding: latin1
def main():

    num1 = input("Dime un número\n")
    
    num2 = input("Dime otro número\n")

    if int(num1)>int(num2):
        print("El número " + str(num1) + " es mayor que el número " + str(num2))
    else:
        print("El número " + str(num2) + " es mayor que el número " + str(num1))

if __name__ == "__main__":
    main()
