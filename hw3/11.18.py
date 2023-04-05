numbers = input()

numbers_list = numbers.split()

int_numbers = []
for i in numbers_list:
    int_numbers.append(int(i))

non_neg_numbers = []
for i in int_numbers:
    if i >= 0:
        non_neg_numbers.append(i)
    else:
        continue

non_neg_numbers.sort()

for i in non_neg_numbers:
    print(i, end=' ')
