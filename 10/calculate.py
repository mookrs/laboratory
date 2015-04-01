# coding: utf-8

import math

sum = 0

for k in xrange(1,1000001):
    sum = sum + math.pow(-1, k + 1) / float((2 * k - 1))

print 4 * sum