import random

numbers = [random.randint(0,10) for i in range(random.randint(5,10))]
print(f'{numbers} ->', end = ' ')
sum_of_odd_index = 0
print("На нечетных позициях элементы:", end = ' ')
for i in range(len(numbers)):
    if i % 2:
        sum_of_odd_index += numbers[i]
        print(numbers[i], end = ' ')
print(f'-> ответ: {sum_of_odd_index}')
