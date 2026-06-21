def additon(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def exponent(num1, num2):
    return num1**num2


def main():
    print("===============Calculator===============")

    while True:
        num1 = float(input("Enter num1 :"))
        num2 = float(input("Enter num2 :"))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponent")
        print("6. Exit")

        operation = int(input("Which operation you want to perform. "))

        if operation == 1:
            print("Addition - ", additon(num1, num2))
        elif operation == 2:
            print("Subtraction - ", subtraction(num1, num2))
        elif operation == 3:
            print("Multiplication - ", multiplication(num1, num2))
        elif operation == 4:
            print("Division - ", divide(num1, num2))
        elif operation == 5:
            print("Exponent - ", exponent(num1, num2))
        elif operation == 6:
            print("Exiting............")
            break


if __name__ == "__main__":

    main()
