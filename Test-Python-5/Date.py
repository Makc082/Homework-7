from datetime import date

def date_differens(year1, month1, day1, year2, month2, day2):

    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)

    difference = abs((date2 - date1).days)
    
    return difference
    
days = date_differens(2024, 2, 17, 2025, 3, 25)
print(days)