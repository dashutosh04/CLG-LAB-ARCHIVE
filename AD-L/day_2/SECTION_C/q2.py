string_ = input("Enter a string: ")

reversed_string = ""
for char in string_:
    reversed_string = char + reversed_string

print(f"Reversed string: {reversed_string}")