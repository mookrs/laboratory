# coding: utf-8

def running_sum(alist):
    total = 0
    for item in alist:
        total += item
        yield total

a = range(20)
print a
print list(running_sum(a))