#hamid Chaker 2060843

def is_palindrome(word):
    new_word = word.replace(' ', '')
    if new_word == new_word[::-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

word = input()
is_palindrome(word)







