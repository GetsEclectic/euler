

def getCollatzSequenceLength(x):
    sequenceLength = 1
    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x = 3 * x + 1
        sequenceLength += 1

    return sequenceLength

longestSequenceSeed = 1
longestSequenceLength = 1
for x in xrange(1,1000000):
    collatzLength = getCollatzSequenceLength(x)

    if collatzLength > longestSequenceLength:
        longestSequenceLength = collatzLength
        longestSequenceSeed = x

print longestSequenceSeed