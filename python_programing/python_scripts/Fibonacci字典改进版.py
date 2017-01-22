# -*- coding:utf8 -*-

import sys

previous = {0: 1, 1: 1}


def fib(n):
    if previous.has_key(n):
        return previous[n]
    else:
        new_value = fib(n - 1) + fib(n - 2)
        previous[n] = new_value
        return new_value

if __name__ == '__main__':
    print fib(int(sys.argv[1]))
