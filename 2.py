# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

numbers = [random.randint(0,10) for i in range(random.randint(2,10))]
total_list = [] # выходной список
print(f'{numbers} => ', end = ' ')

# проверка размера списка (заполняются по-разному)
if len(numbers) % 2:  # нечетная размерность
   for i in range(len(numbers) // 2 + 1):
        total_list.append(numbers[i] * numbers[len(numbers) - i - 1])
else: # четная размерность
    for i in range(len(numbers) // 2):
        total_list.append(numbers[i] * numbers[len(numbers) - i - 1])

print(total_list)
