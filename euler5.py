__author__ = 'ben'
from math import sqrt


def getPrimeDecomposition(product):
    primeDecomp = {}
    for x in xrange(2,product+1):
        while product % x == 0:
            product = product / x
            if x in primeDecomp:
                primeDecomp[x] += 1
            else:
                primeDecomp[x] = 1

    return primeDecomp

lcmPrimeDecomp = {}
for x in xrange(2,20):
    primeDecomp = getPrimeDecomposition(x)
    for key in primeDecomp:
        if key in lcmPrimeDecomp:
            if primeDecomp[key] > lcmPrimeDecomp[key]:
                lcmPrimeDecomp[key] = primeDecomp[key]
        else:
            lcmPrimeDecomp[key] = primeDecomp[key]

print lcmPrimeDecomp

total = 1
for key in lcmPrimeDecomp:
    total *= key ** lcmPrimeDecomp[key]
print total