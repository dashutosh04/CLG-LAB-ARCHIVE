string_ = input("Enter a string: ")

special_char = "~!@#$%^&*()_+`-=/><,.:'; "

for char in string_:
    if char in special_char:
        string_ = string_.replace(char, "")

print(string_)
