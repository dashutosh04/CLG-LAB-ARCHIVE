int_string = input("Enter a string: ")


for char in int_string:
    if char.lower() in "aeiou":
        int_string = int_string.replace(char, "*")

print(int_string)
