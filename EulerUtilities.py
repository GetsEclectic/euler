def getPrimeDecomposition(product):
    primeDecomp = {}
    for x in xrange(2, int(round(product / 2)) + 1):
        while product % x == 0:
            product /= x
            if x in primeDecomp:
                primeDecomp[x] += 1
            else:
                primeDecomp[x] = 1
        if product == 1:
            break

    if not primeDecomp:
        primeDecomp[product] = 1

    return primeDecomp


def generateTriangle(x):
    return x * (x + 1) / 2


def calculateNumDivisorsFromPrimeDecomp(primeDecomp):
    numDivisors = 1

    for key in primeDecomp:
        numDivisors *= primeDecomp[key] + 1

    return numDivisors

def isPythagoreanTriplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2