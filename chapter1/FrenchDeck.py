"""
magic method:__len__() 、__getitem__()
实用胜于纯粹
author:wanggis
"""

import collections
from random import choice

# 以len(x)为例，如果x是一个内置类型的实例，其背后的原因是Cpython 会直接从一个C结构体里面读取对象的长度，完全不会调用任何的方法，可以理解为走了后门


# 创建一个简单的类来表示一张纸牌， namedtuple用于构建只有少数属性但是没有方法的对象
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)]+list('JQKA')
    suits = "spades diamonds clubs hearts".split()    # 分别表示四种花色：黑桃，红心，方块，梅花

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]


    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]



### test  ###


# 构建一个纸牌对象
beer_card = Card('7', "diamonds")
print(beer_card)


# 构建一副完整的纸牌
deck = FrenchDeck()
print(len(deck))


# 从纸牌中抽出指定的一张纸牌

print(deck[0])
print(deck[-1])


# 实现在线随机发牌

player1 = choice(deck)

player2 = choice(deck)



# 利用__getitem__()实现切片操作

print(deck[:3])

print(deck[12::13])   # 切片操作详见 chapter2 ：sclice.py
# 迭代发牌
for card in deck:
    print(card)

# 反向迭代
for card in reversed(deck):
    print(card)




# 利用in和类的迭代，实现扑克检查
print(Card('Q', "hearts") in deck)

print(Card('Q', "beasts") in deck)



# 实现纸牌的大小排序：2最小，A最大。花色上，黑桃最大，红桃次之，方块再次，梅花最小

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values)+suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)



