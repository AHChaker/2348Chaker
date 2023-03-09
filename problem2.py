# take input date from the user and return date if input date is in correct format, else will return empty string
def get_date(date):
    correct = 0
    new_date = ""
    if date.find(",") != -1:
        month_day, year = date.split(',')
        if month_day.find(" ") != -1:
            month, day = month_day.split(" ")
            correct = 1
            day = day.strip()
            month = month.strip()
            year = year.strip()
