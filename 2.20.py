print('Enter amount of lemon juice (in cups):')
lemon_juice = float(input())
print('Enter amount of water (in cups):')
water = float(input())
print('Enter amount of agave nectar (in cups):')
agave_nectar = float(input())
print('How many servings does this make?')
serving_size = float(input())
print('')
print('Lemonade ingredients - yields {:.2f} servings' .format(serving_size))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar))
print('')
print('How many servings would you like to make?')


serving_req = int(input())
print('')
lemon_serving = (serving_req/serving_size)*lemon_juice
water_serving = (serving_req/serving_size)*water
agave_serving = (serving_req/serving_size)*agave_nectar

print('Lemonade ingredients - yields {:.2f} servings'.format(serving_req))
print('{:.2f} cup(s) lemon juice'.format(lemon_serving))
print('{:.2f} cup(s) water'.format(water_serving))
print('{:.2f} cup(s) agave nectar'.format(agave_serving))

lemon_gallons = lemon_serving / 16
water_gallons = water_serving / 16
agave_gallons = agave_serving / 16
print('')
print('Lemonade ingredients - yields {:.2f} servings'.format(serving_req))
print('{:.2f} gallon(s) lemon juice'.format(lemon_gallons))
print('{:.2f} gallon(s) water'.format(water_gallons))
print('{:.2f} gallon(s) agave nectar'.format(agave_gallons))



