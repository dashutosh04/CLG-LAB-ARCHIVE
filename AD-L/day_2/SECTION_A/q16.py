num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def remainder(a, b):
    return a - (a // b) * b


print("Remainder is", remainder(num1, num2))
