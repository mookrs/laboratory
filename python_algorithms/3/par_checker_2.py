import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from stack import Stack


def par_checker_2(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


print(par_checker_2('{{([][])}()}'))
print(par_checker_2('[{()]'))
