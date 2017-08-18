"""
    写三个函数来计算列表中数字的和：分别用 for 循环，while 循环和递归完成。
"""


def while_sum(alist):
    list_lenght = len(alist)
    result = 0
    i = 0
    while i < list_lenght:
        result = result + alist[i]
        i = i + 1
    return result


def for_sum(alist):
    result = 0
    for x in alist:
        result = result + x
    return result


def recursion_sum(alist, index):
    if index == -1:
        return 0
    return alist[index] + recursion_sum(alist, index - 1)


alist = [34, 567, 7, 89, 0, 43, 334, 56, 7, 8, 90, 332, 45]

print(while_sum(alist))
print(for_sum(alist))
print(recursion_sum(alist, len(alist) - 1))
