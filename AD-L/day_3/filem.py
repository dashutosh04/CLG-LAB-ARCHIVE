FILENAME = "./samplefile.txt"


def read_file(file):
    file_o = open(file, "r")
    data = file_o.read()
    file_o.close()
    return data


def write_file(file, data):
    file_o = open(file, "w")
    file_o.write(data)
    file_o.close()


def append_file(file, data):
    file_o = open(file, "a")
    file_o.write(data)
    file_o.close()


with open(FILENAME, "r") as file:
    content = file.read()
    print(content)

for line in open(FILENAME):
    print(line)


with open(FILENAME, "r") as file:
    lines = file.readlines()
    print(lines)

with open(FILENAME, "r") as file:
    line = file.readline()
    print(line)

with open(FILENAME, "w") as file:
    file.write("Anything can be written here and will be overwritten.")

with open(FILENAME, "a") as file:
    file.write("\nAppended line. ")


practicalfile = open(FILENAME, "a")
practicalfile.write("Writing in the file")
practicalfile.close()

append_file(FILENAME, "\nAppended using function.")
data = read_file(FILENAME)
print(data)
write_file(FILENAME, "Overwritten using function.")
data = read_file(FILENAME)
print(data)
append_file(FILENAME, "\nAppended again using function.")
data = read_file(FILENAME)
print(data)
