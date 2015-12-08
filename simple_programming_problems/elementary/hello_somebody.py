#!/usr/bin/env python
# -*- coding: utf-8 -*-

is_somebody = False
while not is_somebody:
    name = raw_input("Please input your name: ")
    if name == 'Alice' or name == 'Bob':
        print "hello, %s" % name
        is_somebody = True
    else:
        print 'You are not Alice nor Bob! Input again.'