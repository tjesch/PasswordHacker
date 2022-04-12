#  You can experiment here, it won’t be checked
import itertools

sample = 'abcdef123'
def fun(x):
    print(x)
    print(sample.upper())
    return x.upper()

print(fun(sample))

print(itertools.product(sample, fun))
