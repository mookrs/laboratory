#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
has_guess_right = False
guess_count = 0
answer = int(random.uniform(1, 100))
last_guess = None
while not has_guess_right:
    input_num = raw_input('Please input a number: ')
    if int(input_num) != last_guess:
        guess_count = guess_count + 1
    last_guess = int(input_num)
    if int(input_num) > answer:
        print 'It is big!'
    elif int(input_num) < answer:
        print 'It is small!'
    else:
        print 'Right!'
        has_guess_right = True

print 'You are out! You have guess %d times' % guess_count