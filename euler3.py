product = 600851475143
largestPrimeFactor = 1
for x in xrange(2,int(round(product/2))):
    while product % x == 0:
        product = product / x
        largestPrimeFactor = x
    if product == 1:
        break
print x