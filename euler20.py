import math

bigNum = math.factorial(100)
total = 0
for digit in str(bigNum):
    total += int(digit)

print total