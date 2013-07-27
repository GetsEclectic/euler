def isPrime(x):
    isPrime = False
    for i in xrange(2,int(round(x/2))+1):
        if x % i == 0:
            break
    else:
        isPrime = True
    return  isPrime

primeToFind = 10001
primes = []
x = 2
while len(primes) < primeToFind:
    if isPrime(x):
        primes.append(x)
    x += 1

print primes[primeToFind - 1]