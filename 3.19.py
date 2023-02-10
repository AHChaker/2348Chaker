# Hamid Chaker 2060843
print('Enter wall height (feet):')
wall_h = int(input())
print('Enter wall width (feet):')
wall_w = int(input())
wall_area = wall_h * wall_w
print('Wall area:', wall_area, 'square feet')

paint_gallons = wall_area / 350
print('Paint needed:', f'{paint_gallons:.2f}', 'gallons')
cans = round(paint_gallons)
print('Cans needed:', cans, 'can(s)')
print('')
print('Choose a color to paint the wall:')
color = input()
colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}
print(f'Cost of purchasing {color} paint: ${colors[color]*cans}')
