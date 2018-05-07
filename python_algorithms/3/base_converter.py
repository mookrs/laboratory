import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from stack import Stack


def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        remstack.push(rem)
        dec_number = dec_number // base

    new_string = ''
    while not remstack.is_empty():
        new_string = new_string + digits[remstack.pop()]

    return new_string

print(base_converter(25, 2))
print(base_converter(25, 16))
