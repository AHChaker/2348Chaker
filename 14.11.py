#Hamid Chaker 2060843
def selection_sort_descend_trace(num):
    for i in range(len(num) - 1):
        max = i
        for j in range(i+1, len(num)):
            if num[j] > num[max]:
                max= j
        num[i], num[max] = num[max], num[i]
        print(' '.join(str(i) for i in num), end=' \n')


if __name__ == '__main__':
    numbers_list = input()
    numbers = [i for i in numbers_list.split()]
    selection_sort_descend_trace(numbers)