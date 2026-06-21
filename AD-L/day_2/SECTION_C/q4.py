string_ = input("Enter a stirng: ")
string_dict = {}

for char in string_:
    if char in string_dict:
        string_dict[char] += 1
    else:
        string_dict[char] = 1

for key in string_dict:
    print(f"Frequency of {key} - {string_dict[key]}")
