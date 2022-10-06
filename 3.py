# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

numbers = [round(random.uniform(-10,10), 2) for i in range(random.randint(2, 5))]
fraction_list = [] # список дробных частей изначального списка
print(f'{numbers} => ', end = ' ')

for i in numbers:
    fraction_list.append(abs(i) - int(abs(i))) # смотрим по модулю

print(round(max(fraction_list) - min(fraction_list), 2))
