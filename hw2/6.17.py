# Hamid Chaker 2060843
pw = input()

password = ''

for letter in pw:

    if (letter == 'i'):
        password += '!'
    elif (letter == 'a'):
        password += '@'
    elif (letter == 'm'):
        password += 'M'
    elif (letter == 'B'):
        password += '8'
    elif (letter == 'o'):
        password += '.'
    else:
        password += letter

print(password + "q*s")
