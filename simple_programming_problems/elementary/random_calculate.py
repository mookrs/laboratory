# coding: utf-8
"""
    写个程序，要求用户输入一个数 n，并概率性的选择是计算 1 到 n 的和还是计算 1 到 n 的乘积。
"""

import random


def sum_n(n):
    return sum([i for i in xrange(n)])


def factorial_n(n):
    if n == 0:
        return 1
    else:
        return n * factorial_n(n - 1)

n = raw_input('Please input an integer: ')
if random.random() < 0.5:
    print sum_n(int(n))
else:
    print factorial_n(int(n))
