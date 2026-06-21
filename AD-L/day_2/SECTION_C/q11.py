string_ = input("enter a string: ")

string_ = list(string_)

for i in range(len(string_)):
    if i == 0 or string_[i - 1] == " ":
        string_[i] = chr(ord(string_[i]) - 32)


print("".join(string_))
    