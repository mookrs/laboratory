# coding: utf-8
"""
    写程序计算一个和式。
"""

import math

print 4 * sum(math.pow(-1, k + 1) / float((2 * k - 1)) for k in xrange(1, 1000001))
