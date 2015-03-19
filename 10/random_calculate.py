#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def sum_n(n):
    return sum([i for i in xrange(n)])

def factorial_n(n):
    if n == 0:
        return 1
    else:
        return n * factorial_n(n-1)

n = raw_input('Please input an integer: ')
if random.random() < 0.5:
    print sum_n(int(n))
else:
    print factorial_n(int(n))