#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = raw_input("Please input a number: ")
sum = 0
for i in xrange(1, int(num)):
    if not (i % 3 and i % 5):
        sum = sum + i
print sum