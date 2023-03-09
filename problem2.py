#hamid chaker 2060843
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