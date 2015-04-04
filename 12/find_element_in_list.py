# coding: utf-8

def is_in_list(alist, element):
    is_in = False
    for x in alist:
        if x == element:
            is_in = True
            break
    return is_in

print is_in_list([23,45,67,8,9,2], 3)
print is_in_list([23,45,67,8,9,2], 9)