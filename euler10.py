__author__ = 'ben'
from math import sqrt
listOfPrimes = [2]

total = 2
for x in xrange(3, 2000000, 2):
    for prime in listOfPrimes:
        if x % prime == 0:
            break
        if prime > sqrt(x):
            listOfPrimes.append(x)
            total += x
            break
    if (x - 1) % 10000 == 0:
        print x

print total