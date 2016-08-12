# Newton-Raphson method
k = 24.0
eplison = 0.01
numGuesses = 0
guess = k / 2.0
diff = guess ** 2 - k
while abs(diff) > eplison:
    guess = guess - diff / (2 * guess)
    diff = guess ** 2 - k
    numGuesses += 1
print('numGuesses =', numGuesses)
print('Square root of', k, 'is about', guess)
