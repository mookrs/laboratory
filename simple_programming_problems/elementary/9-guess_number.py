"""
    写一个竞猜游戏，用户必须猜一个秘密的数字，在每次猜完后程序会告诉用户他猜的数是太大了还是太小了，
    直到猜测正确，最后打印出猜测的次数。如果用户连续猜测同一个数字则只算一次。
"""
import random

guess_right = False
guess_count = 0
answer = random.randint(1, 100)
last_guess = None

while not guess_right:
    input_num = input('Please input a number: ')
    if int(input_num) != last_guess:
        guess_count += 1
    last_guess = int(input_num)

    if int(input_num) > answer:
        print('It is big!')
    elif int(input_num) < answer:
        print('It is small!')
    else:
        print('Right!')
        guess_right = True

print('You are out! You have guess {} times'.format(guess_count))
