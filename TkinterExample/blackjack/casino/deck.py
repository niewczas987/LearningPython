import random
from .card import Card
class Deck:
    def __init__(self):
        # self.cards = [Card(s,v) for s in ['Spades','Clubs','Hearts','Diamonds']
        #               for v in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']]
        self.cards = [Card(s,v) for s in ['s','c','h','d']
                      for v in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']]
    def shuffle(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)
    def deal(self):
        if len(self.cards)>1:
            return self.cards.pop(0)