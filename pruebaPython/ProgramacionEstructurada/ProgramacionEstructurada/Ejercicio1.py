#coding: latin1
def main():

    num1 = input("Dime un n�mero\n")
    
    par = "par" if (int(num1)%2 == 0) else "impar"

    print(par)

if __name__ == "__main__":
    main()
