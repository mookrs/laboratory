# -*- coding: utf-8 -*-

with open('apple_middle_format_wandoujia.csv', 'r') as ascending_file, open('apple_middle_format_wandoujia_descending.csv', 'w') as descending_file:
    stack = []
    for line in ascending_file:
        stack.append(line)
    while stack:
        descending_file.write(stack.pop())