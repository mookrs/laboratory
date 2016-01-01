# coding: utf-8
"""
    仅可以与 Alice 和 Bob 这两个用户用其姓名与之打招呼。
"""

is_somebody = False
while not is_somebody:
    name = raw_input("Please input your name: ")
    if name == 'Alice' or name == 'Bob':
        print "hello, %s" % name
        is_somebody = True
    else:
        print 'You are not Alice nor Bob! Input again.'
