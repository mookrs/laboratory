"""
    写程序打印出 12×12 乘法表。
"""

for i in range(1, 13):
    for j in range(1, 13):
        print('{:3}'.format(i * j), end=' ')
    print('\n')
