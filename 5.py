# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

size_of_list = int(input())  # задаем размерность фибоначчи в одну сторону
help_list_pos = [0, 1] # cписок положительных чисел
help_list_neg = [0, 1] # список отрицательных чисел

# заполенение положительного списка Фибоанччи
for i in range(2, size_of_list):
    help_list_pos.append(help_list_pos[i - 2] + help_list_pos[i - 1])

# заполенение отрицательного списка Фибоанччи
for j in range(2, size_of_list):
    help_list_neg.append(help_list_neg[j - 2] - help_list_neg[j - 1])

# разворачиваем отрицательный список Фибоначчи, чтобы соединить
for k in range(size_of_list // 2):
    help_list_neg[k], help_list_neg[size_of_list - k - 1] = help_list_neg[size_of_list - k - 1], help_list_neg[k]

fibonacci_list = help_list_neg + help_list_pos # соединяем список
del[fibonacci_list[len(fibonacci_list) // 2]] # удаляем лишний ноль
print(fibonacci_list)