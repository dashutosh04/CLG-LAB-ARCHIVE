string_ = input("Enter a string: ")

digits = ""

for char in string_:
    if char.isdigit():
        digits += char

print(f"Digits: {digits}")

#

