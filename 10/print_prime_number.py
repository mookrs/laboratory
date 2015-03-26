#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for num in range(2, 101):
    if is_prime(num):
        print num,