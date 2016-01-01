# coding: utf-8
"""
    写个函数计算列表的运行花费总和。
"""


def running_sum(alist):
    total = 0
    for item in alist:
        total += item
        yield total

a = range(20)
print a
print list(running_sum(a))
