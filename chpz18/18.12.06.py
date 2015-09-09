import random

class Card(object):
    """Represents a standard playing card.

    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        """Compares this card to other, first by suit, then rank.

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label=''):
        self.cards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


class PokerHand(Hand):

    types_of_hands = ["has_none", "has_two_of_a_kind", "has_three_of_a_kind", "has_straight", "has_flush", "has_full_house", "has_four_of_a_kind", "has_straight_flush"]

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def rank_hist(self):
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_two_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_three_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False


    def has_straight(self):
        self.rank_hist()
        if 1 in self.ranks.keys():
            self.ranks[14] = 1

        for card in self.cards:
            count = 0
            for i in xrange(5):
                if card.rank + i in self.ranks.keys():
                    count += 1
            if count >= 5:
                return True
        return False


    def has_full_house(self):
        self.rank_hist()

        for x in self.ranks.values():
            for y in self.ranks.values():
                if x >= 3 and y >= 2:
                    return True
        return False


    def has_four_of_a_kind(self):
        self.rank_hist()
        for val in self.ranks.values():
            if val == 4:
                return True
        return False


    def has_straight_flush(self):
        if not self.has_straight() and not self.has_flush():
            return False

        for card in self.cards:
            if card.rank == 1:
                high_ace = Card(card.suit, 14)
                self.cards.append(high_ace)

        for card in self.cards:
            print card
            count = 0
            for i in xrange(1, 5):
                for other_card in self.cards:
                    if other_card.rank == card.rank + i and other_card.suit == card.suit:
                        count += 1
            if count == 4:
                return True
        return False


    def classify(self):
        self.has_hands = []
        best_hand = PokerHand.types_of_hands[0]

        for type in PokerHand.types_of_hands[1:]:
            x = getattr(self, type)
            if x():
                self.has_hands.append(type)

        for item in self.has_hands:
            if self.types_of_hands.index(item) > self.types_of_hands.index(best_hand):
                best_hand = item

        self.label = best_hand


def find_probabilities(num_of_decks):
    probability_histo = {}
    total_num_hands = num_of_decks * 7

    for num in xrange(num_of_decks):
        deck = Deck()
        deck.shuffle()

        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.classify()
            for item in hand.has_hands:
                probability_histo[item] = probability_histo.get(item, 0) + 1

    for type_hand in probability_histo.keys():
        probability_histo[type_hand] = str(probability_histo[type_hand] / float(total_num_hands) * 100) + " %"

    print probability_histo


find_probabilities(10000)
