squareOfSums = (100 * 101 / 2) ** 2
sumOfSquares = 0
for x in xrange(1, 101):
    sumOfSquares += x ** 2
print squareOfSums - sumOfSquares