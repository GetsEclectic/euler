palindromeProduct = 1
for x in xrange(999,1,-1):
    for y in xrange(999,1,-1):
        product = x * y
        if str(product) == str(product)[::-1] and product > palindromeProduct:
            palindromeProduct = product
print palindromeProduct