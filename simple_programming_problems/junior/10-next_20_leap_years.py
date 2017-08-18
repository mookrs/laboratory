"""
    写个程序打印出接下来的 20 个闰年。
"""
from datetime import datetime


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False


this_year = datetime.now().year
leap_years = []

for _ in range(0, 20):
    while not is_leap_year(this_year):
        this_year += 1

    leap_years.append(this_year)
    this_year += 1

print(leap_years)
