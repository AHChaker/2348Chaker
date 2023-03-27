# Hamid Chaker 2060843
print("Birthday Calculator")

print("Current date")
this_month = int(input("Month: "))
this_day = int(input("Day: "))
this_year = int(input("Year: "))

print("Birthday")
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))
birth_year = int(input("Year: "))

age = this_year - birth_year
if (this_month, this_day) < (birth_month, birth_day):
    age -= 1

print("You are", age, "years old.")

if this_day == birth_day and this_month == birth_month:
    print('Happy Birthday!')