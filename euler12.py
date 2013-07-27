__author__ = 'ben'
import time
from EulerUtilities import *


x = 1
while calculateNumDivisorsFromPrimeDecomp(getPrimeDecomposition(generateTriangle(x))) <= 500:
    x += 1
    if x % 1000 == 0:
        print generateTriangle(x)
        print calculateNumDivisorsFromPrimeDecomp(getPrimeDecomposition(generateTriangle(x)))
print generateTriangle(x)
print calculateNumDivisorsFromPrimeDecomp(getPrimeDecomposition(generateTriangle(x)))