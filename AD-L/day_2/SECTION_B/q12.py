def isprime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


number = int(input("Count primes till ? "))

count = 0
for i in range(1, number + 1):
    if isprime(i):
        count = count + 1

print(f"Count: {count}")
