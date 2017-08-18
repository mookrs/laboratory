"""
    仅可以与 Alice 和 Bob 这两个用户用其姓名与之打招呼。
"""

is_somebody = False
while not is_somebody:
    name = input('Please input your name: ')
    if name == 'Alice' or name == 'Bob':
        print('Hello, {}.'.format(name))
        is_somebody = True
    else:
        print('You are not Alice nor Bob! Input again.')
