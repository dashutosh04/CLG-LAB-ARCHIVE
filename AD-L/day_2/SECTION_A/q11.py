year_int = int(input("Enter a year: "))

if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
    print(f"{year_int} is a leap year.")
else:
    print(f"{year_int} is not a leap year.")