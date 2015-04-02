# coding: utf-8

def find_max_in_list(alist):
    max = alist[0]
    for num in alist:
        if num > max:
            max = num
    print max

alist = [23,45,6547,78,88,9,9,0,22234,33]
find_max_in_list(alist)