number = int(input("Enter a number: "))

while number > 0:
    digit = number % 10
    if digit % 3 == 0:
        print(digit)
    number = number // 10
