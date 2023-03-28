print('Enter player 1\'s jersey number:')
jersey1 = int(input())
print('Enter player 1\'s rating:')
rating1 = int(input())
print('')
print('Enter player 2\'s jersey number:')
jersey2 = int(input())
print('Enter player 2\'s rating:')
rating2 = int(input())
print('')
print('Enter player 3\'s jersey number:')
jersey3 = int(input())
print('Enter player 3\'s rating:')
rating3 = int(input())
print('')
print('Enter player 4\'s jersey number:')
jersey4 = int(input())
print('Enter player 4\'s rating:')
rating4 = int(input())
print('')
print('Enter player 5\'s jersey number:')
jersey5 = int(input())
print('Enter player 5\'s rating:')
rating5 = int(input())
print('')


player_dict = {
    jersey1: rating1,
    jersey2: rating2,
    jersey3: rating3,
    jersey4: rating4,
    jersey5: rating5
        }

player_dict = dict(sorted(player_dict.items()))

print("ROSTER")
for num, rate in player_dict.items():
    print(f'Jersey number: {num}, Rating: {rate}')

print()

print("MENU")
print("a - Add player")
print("d - Remove player")
print("u - Update player rating")
print("r - Output players above a rating")
print("o - Output roster")
print("q - Quit")
print()
print("Choose an option:")

user_input = str(input())

while user_input != "q":
    print('')
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    print("Choose an option:")
    user_input = str(input())
    if user_input == 'o':
        print("ROSTER")
        for num, rate in player_dict.items():
            print(f'Jersey number: {num}, Rating: {rate}')
    elif user_input == 'a':
        print('Enter a new player\'s jersey number')
        new_jersey = int(input())
        print('Enter a new player\'s rating')
        new_rate = int(input())
        player_dict.update({new_jersey: new_rate})
    elif user_input == 'd':
        print('Enter a jersey number')
        del_jersey = int(input())
        player_dict.pop(del_jersey)