# -*- coding: utf-8 -*-

with open('middle_format_nokia(labi+Nokia phone number error).csv', 'r') as old_file, open('middle_nokia.csv', 'w') as new_file:
    for line in old_file:
        new_file.write(line.rstrip() + ',nokia\n')