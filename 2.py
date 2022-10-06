import random

numbers = [random.randint(0,10) for i in range(random.randint(2,4))]
total_list = []
print(f'{numbers} => ', end = ' ')
if len(numbers) % 2:
   for i in range(len(numbers) // 2 + 1):
        total_list.append(numbers[i] * numbers[len(numbers) - i - 1])
else:
    for i in range(len(numbers) // 2):
        total_list.append(numbers[i] * numbers[len(numbers) - i - 1])
print(total_list)
