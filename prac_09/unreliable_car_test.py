from unreliable_car import UnreliableCar

new_car_numero_uno = UnreliableCar("Car one", 100, 50)
new_car_numero_uno.drive(50)
print(new_car_numero_uno)
new_car_numero_uno.drive(60)
print(new_car_numero_uno)

number_of_tests = 200

new_car_numero_dos = UnreliableCar("Car two", number_of_tests, 60)  # 100 - 60 = 40% reliable car
for i in range(number_of_tests):
    distance = new_car_numero_dos.drive(1)
print(f"Car two succeeded approx %{new_car_numero_dos.fuel / number_of_tests * 100} of the time")
