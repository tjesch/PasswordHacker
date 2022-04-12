#  You can experiment here, it won’t be checked
import itertools
import string
possible_chars = itertools.chain(string.ascii_lowercase, string.digits)
my_iter = map(lambda x: 'AB' + x,possible_chars)
print(list(my_iter))
