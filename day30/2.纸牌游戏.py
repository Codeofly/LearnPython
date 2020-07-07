from collections import namedtuple
Card = namedtuple('Card',['rank','suit'])
class FranchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = ['红心','方板','梅花','黑桃']

    def __init__(self):
        self._cards = [Card(rank,suit) for rank in FranchDeck.ranks
                                        for suit in FranchDeck.suits]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value
#
# deck = FranchDeck()
# print(deck._cards)
# print(deck._cards[0:10])
# print(deck[0])   # item
# from random import choice
# print(choice(deck))
# print(choice(deck))
# print(choice(deck))
# print(choice(deck))
# print(choice(deck))

# 内置的模块 和内置的函数 和 内置的方法

# from random import shuffle
# shuffle(deck)
# print(deck[:])

# from random import sample
# print(sample(deck[:],2))