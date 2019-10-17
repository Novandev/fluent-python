import collections
from random import choice,shuffle
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # This should be a list of numers 1-11 as well as the face carsd
    suits = 'spades diamonds clubs hearts'.split() # Spliting this string based onthe names of the suits
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] #for everyone one of the sutes, create all cards 1-11 and the face cards
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    #  test_card = Card('3', 'clubs')
    #  print(test_card)

     test_deck = FrenchDeck()
     print(len(test_deck))
     print(test_deck[1])
     print(choice(test_deck))
     print(test_deck[1:10])