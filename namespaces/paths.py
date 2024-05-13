# приведёт к ModuleNotFoundError
# import _poker

from sys import path

print(*path, sep='\n')

path.insert(1, r'd:\G-Doc\TOP Academy\Data Science\422\scripts\functional')

import _poker

hand = (2, 3, 4, 5, 6)
print('', hand, _poker.poker_combination(hand), sep='\n')
