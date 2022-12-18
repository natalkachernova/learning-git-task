print("Модуль 3. Завдання 2")
result_numbers = []
result_numbers_in_cube = []

for i in range(101):
    if i % 5 == 0:
        result_numbers.append(i)
        result_numbers_in_cube.append(i ** 3)        

print(result_numbers)
print(result_numbers_in_cube)
