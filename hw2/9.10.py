#hamid chaker 2060843
import csv
csv_input = input()

with open(csv_input, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        words_list = row


no_duplicates = list(dict.fromkeys(words_list))
listlength = len(no_duplicates)

for i in range(listlength):
    print(no_duplicates[i], words_list.count(no_duplicates[i]))
