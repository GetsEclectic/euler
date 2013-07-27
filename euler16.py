from operator import add

twoToTheOneThousand = str(2 ** 1000)
castToIntAndAdd = lambda x, y: add(int(x), int(y))
print reduce(castToIntAndAdd, twoToTheOneThousand, 0)
