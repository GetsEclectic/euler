__author__ = 'ben'
from EulerUtilities import *

print isPythagoreanTriplet(3, 4, 5)

for a in xrange(1, 999):
    for b in xrange(1, 999):
        if isPythagoreanTriplet(a, b, 1000 - a - b):
            print "a: {} b: {} c: {}".format(a, b, 1000 - a - b)
            print "a*b*c: {}".format(a * b * (1000 - a - b))
            quit()