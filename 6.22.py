# Hamid Chaker 2060843
x1 = int(input())
y1 = int(input())
t1 = int(input())
x2 = int(input())
y2 = int(input())
t2 = int(input())

fals_var = False
for num in range(-10, 11):
    for num2 in range(-10, 11):
        if (x1*num) + (y1*num2) == t1 and (x2*num) + (y2*num2) == t2:
            print(num, num2)
            fals_var = True

if fals_var == False:
    print("No solution")

