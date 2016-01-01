# coding: utf-8
"""
    写程序输入一个数 n 并打印出从 1 到 n 的和，但要使得求和的数只包含 3 或 5 的倍数，
    例如 n=17，则求和的数为：3, 5, 6, 9, 10, 12, 15。
"""

num = raw_input("Please input a number: ")
print sum([i for i in xrange(int(num)) if not (i % 3 and i % 5)])
