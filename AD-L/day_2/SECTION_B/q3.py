sum = 0
sum_till = int(input("Sum till which number ?"))

for i in range(1, sum_till + 1):
    sum += i
print(f"Sum from 1 to {sum_till} is: {sum}")
