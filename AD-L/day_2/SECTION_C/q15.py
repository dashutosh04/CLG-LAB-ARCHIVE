string_ = input("Enter a string: ")

char_dict = {}

for char in string_:
    if char in char_dict:
        char_dict[char] += 1
    else:
        char_dict[char] = 1

print(char_dict)
print(max(char_dict, key=char_dict.get))
