words = input()

list_words = words.split()

for i in list_words:
    print(i, list_words.count(i))