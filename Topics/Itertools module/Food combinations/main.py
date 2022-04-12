#  You can experiment here, it won’t be checked
import itertools
password = 'abc'
for word in itertools.product([letter.upper(), letter.lower()] for letter in password):
    print(word)
worder = itertools.product([letter.upper(), letter.lower()] for letter in password)

print(list(worder))
wordest = itertools.product(*([letter.upper(), letter.lower()] for letter in password))
print('lister')
print(*([letter.upper(), letter.lower()] for letter in password))
print(list(wordest))
print('prodtest')
print(list(itertools.product([['a','b'],['0','1'],['c','d']])))
print('prodtest2')
print(list(itertools.product(*[['a','b'],['0','1'],['c','d']])))
print('mapper')
#print(list(itertools.starmap(lambda x: ''.join(x), [(['a', 'b'],), (['0', '1'],), (['c','d'],)])))
#print(list(itertools.starmap(lambda x: ''.join(x), [['A', 'a'], ['B', 'b'], ['C', 'c']])))
#print(list(map(lambda x: ''.join(x), [(['A', 'a'],), (['B', 'b'],), (['C', 'c'],)])))

new_words = map(lambda x: ''.join(x), itertools.product(*([letter.upper(), letter.lower()] for letter in password)))
print(list(new_words))

packed = [[1,2],[3,4]]
print(packed)
print(*packed)
