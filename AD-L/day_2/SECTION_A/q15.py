number = int(input("Enter a number: "))
print("Original:", number)
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10


print("Reversed:", reversed_num)
