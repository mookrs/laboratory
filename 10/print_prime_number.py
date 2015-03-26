#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, math

def print_prime_number(num):
    prime_list = [2]
    current_number = 3
    while current_number < num:
        is_prime = True
        current_sqrt = math.floor(math.sqrt(current_number))
        i = 0

        while i >= len(prime_list) or prime_list[i] < current_sqrt:
            if current_number % prime_list[i] == 0:
                is_prime = False
                break
            i = i + 1

        if is_prime:
            prime_list.append(current_number)
        current_number = current_number + 1
    
    print prime_list


print_prime_number(44)