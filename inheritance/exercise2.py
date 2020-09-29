import random

class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace','2','3','4','5','6','7',
                    '8', '9','10','Jack','Queen','King']
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'
    def __lt__(self, other):
        return self.suit < other.suit
    def __eq__(self, other):
        if self.suit == other.suit:
            return self.rank == other.rank
        else: return False

class Deck(object):
    def __init__(self):
        self.cards =[]
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self,card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        return self.cards.sort(key= lambda card: card.suit *12 + card.rank )

deck = Deck()
deck.shuffle()
print(deck)
deck.sort()
print(deck)