# -*- coding:utf8 -*-


def print_multiples(n, high):
    i = 1
    while i <= high:
        print n * i, '\t',
        i = i + 1
    print


def print_multiplication_table(high):
    i = 1
    while i <= high:
        print_multiples(i, i)
        i = i + 1

if __name__ == '__main__':
    print_multiplication_table(6)
