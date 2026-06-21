def multiply_function(a, b):
    result = a * b
    result2 = result * result
    return result, result2


numbers_list = [1, 2, 3]
multiplier_list = [2, 4]

for n in numbers_list:
    print("------------------------")
    for m in multiplier_list:
        current_answer, current_answer2 = multiply_function(n, m)
        print(f"The answer to {n} x {m} is:  {current_answer}")
        print(f"The result of this squared is:  {current_answer2}")
