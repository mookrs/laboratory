# coding: utf-8
"""
    写程序打印出 12×12 乘法表。
"""

for i in xrange(1, 13):
    for j in xrange(1, 13):
        print '{:3}'.format(i * j),
    print '\n'