auto_shop = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    "-": 0
}
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print("")

print("Select first service:")
first_serv = str(input())
print("Select second service:")
second_serv = str(input())

print("")
print("Davy's auto shop invoice")
print("")
if first_serv == '-':
    print('Service 1: No service' )
    print(f'Service 2: {second_serv}, ${auto_shop[second_serv]}')
elif second_serv == '-':
    print(f'Service 1: {first_serv}, ${auto_shop[first_serv]}')
    print('Service 2: No service' )
elif first_serv == '-' and second_serv == '-':
    print('Service 1: No service' )
    print('Service 2: No service' )
else:
    print(f'Service 1: {first_serv}, ${auto_shop[first_serv]}')
    print(f'Service 2: {second_serv}, ${auto_shop[second_serv]}')

print("")
print(f'Total: ${auto_shop[first_serv]+auto_shop[second_serv]}')



