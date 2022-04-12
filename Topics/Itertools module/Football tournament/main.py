# the variable 'teams' is already defined
import itertools
#teams = ['Best-ever', 'Not-so-good', 'Amateurs']
my_iter = itertools.combinations(teams, 2)

for combo in my_iter:
    print(combo)

