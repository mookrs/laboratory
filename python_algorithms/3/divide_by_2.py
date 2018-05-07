import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from stack import Stack


def divide_by_2(dec_number):
    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number = dec_number // 2

    bin_string = ''
    while not remstack.is_empty():
        bin_string = bin_string + str(remstack.pop())

    return bin_string

print(divide_by_2(42))
