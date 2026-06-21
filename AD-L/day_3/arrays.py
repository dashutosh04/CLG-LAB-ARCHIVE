cars = ["Ford ", "Volvo ", "BMW ", "Toyota ", "Maruti ", "Audi ", "Kia ", "Hyundai "]
print(cars)

cars.append("Honda ")
print(cars)

cars.pop(5)
print(cars)

cars.remove("Volvo ")
print(cars)

print(cars.count("Ford "))

cars.extend(["Jeep ", "Tata "])
print(cars)

cars.reverse()
print(cars)

cars.index("Toyota ")
print(cars)

cars[7] = cars.copy()[4]
print(cars)

cars.sort()
print(cars)

cars.clear()
print(cars)
