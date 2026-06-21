int_string = input("Enter a string: ")

count = 0
for char in int_string:
    if char.lower() in "aeiou":
        count = count + 1

print(f"Number of vowels: {count}")
