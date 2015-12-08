# coding: utf-8

from datetime import datetime

this_year = datetime.now().year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


years_count = 0
leap_years = []

while years_count < 20:
    while not is_leap_year(this_year):
        this_year = this_year + 1
    leap_years.append(this_year)
    this_year = this_year + 1
    years_count = years_count + 1

print leap_years