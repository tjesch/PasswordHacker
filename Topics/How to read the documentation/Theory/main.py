#  You can experiment here, it won’t be checked
import itertools
list_letters = ['Q','E','O','F','J','Z','X','V','N','M']

print(list(itertools.product(list_letters, repeat=2)))
print(list(map(lambda x: x + 'ONE',list(map(lambda x: ''.join(x), itertools.product(list_letters, repeat=2))))))

