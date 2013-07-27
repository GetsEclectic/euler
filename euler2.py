previousFib = 1
currentFib = 2
total = 0
while currentFib <= 4000000:
    if currentFib % 2 == 0:
        total += currentFib
    if currentFib < 100:
        print currentFib
    currentFib += previousFib
    previousFib = currentFib - previousFib
print total