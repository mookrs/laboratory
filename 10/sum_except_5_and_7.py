#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = raw_input("Please input a number: ")
print sum([i for i in xrange(int(num)) if not (i % 3 and i % 5)])