#!/usr/bin/env python
# -*- coding: utf-8 -*-

for i in xrange(1, 13):
    for j in xrange(1, 13):
        print '{:3}'.format(i * j),
    print '\n'