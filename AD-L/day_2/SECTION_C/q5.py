string_ = input("enter a string: ")

string_ = list(string_)
for i in range(len(string_)):
    string_[i] = chr(ord(string_[i]) - 32)


print("".join(string_))
