test_string = "quick brown fox jumps over the lazy dog"

print(test_string[0])
print(test_string[1])

print(test_string[-1])

print(test_string[4:])
print(test_string[:4])

print(test_string[2:8])

print(test_string[::-1])


print()
varlist = test_string.split()

for word in varlist[::-1]:
    print(word, end=" ")
