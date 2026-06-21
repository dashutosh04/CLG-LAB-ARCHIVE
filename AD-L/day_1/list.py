numbers = [1, 2, 3, 4, 5]
print("List 1 ", numbers)
print("Type of List 1 ", type(numbers))

arbitary_list = [1, numbers, "hello"]
print("List 2 ", arbitary_list)
print("Type of List 2 ", type(arbitary_list))


print("List 1 ", numbers)

numbers[1] = 5
print("List 1 ", numbers)

numbers.insert(2, 3)
print("List 1", numbers)

numbers.append(4)
print("List 1", numbers)

numbers.remove(3)
print("List 1", numbers)

numbers.remove(3)
print("List 1", numbers)

del numbers[1]

print("List 1", numbers)

del numbers[-1]

print("List 1", numbers)
