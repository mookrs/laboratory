# Keeping the Last N Items
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.appendleft(5)
print(q)
q.pop()
print(q)
q.popleft()
print(q)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        # 遇到 pattern 则 yield 该 pattern 所在行的前 5 行
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
