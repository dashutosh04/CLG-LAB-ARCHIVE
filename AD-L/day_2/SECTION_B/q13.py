sum_odd = 0
sum_even = 0

number = int(input("Enter a number: "))

while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
    number //= 10

print("Sum even", sum_even)
print("Sum odd", sum_odd)