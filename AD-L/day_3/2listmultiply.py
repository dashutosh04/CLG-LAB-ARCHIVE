def multiply(a, b):
    return a * b

list1 = [1, 2, 3]
list2 = [2, 4]

for i in range(len(list1)):
    for j in range(len(list2)):
        print(f"Answer of {list1[i]} * {list2[j]} is {multiply(list1[i], list2[j])}")
    print("------------------------")