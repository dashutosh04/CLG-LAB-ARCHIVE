number = int(input("Enter a number: ")) 

armstrong = 0

temp = number

while temp > 0:
    digit = temp % 10
    armstrong = digit ** 3 + armstrong
    temp //= 10

if armstrong == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")