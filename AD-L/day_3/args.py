def my_function(a, b, /, *, c=0, d=0):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")


my_function(1, 2, c=3, d=4)

