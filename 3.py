import random

numbers = [round(random.uniform(0,10), 2) for i in range(random.randint(2, 5))]
fraction_list = []
print(f'{numbers} => ', end = ' ')
for i in numbers:
    fraction_list.append(i - int(i))
print(round(max(fraction_list) - min(fraction_list), 2))
