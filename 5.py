size_of_list = int(input())
help_list_pos = [0, 1]
help_list_neg = [0, 1]
for i in range(2, size_of_list):
    help_list_pos.append(help_list_pos[i - 2] + help_list_pos[i - 1])
for j in range(2, size_of_list):
    help_list_neg.append(help_list_neg[j - 2] - help_list_neg[j - 1])
for k in range(size_of_list // 2):
    help_list_neg[k], help_list_neg[size_of_list - k - 1] = help_list_neg[size_of_list - k - 1], help_list_neg[k]
fibonacci_list = help_list_neg + help_list_pos
del[fibonacci_list[len(fibonacci_list) // 2]]
print(fibonacci_list)