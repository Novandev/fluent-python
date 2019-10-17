import collection
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # This should be a list of numers 1-11 as well as the non-number cars
    suits = 'spades diamonds clubs hearts'.split() # Spliting this string based onthe names of the suits
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

if __name__ == "__main__":
