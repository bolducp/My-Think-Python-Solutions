"""
Write a Deck method called deal_hands that takes two parameters,
the number of hands and the number of cards per hand, and that creates
new Hand objects, deals the appropriate number of cards per hand,
and returns a list of Hand objects."""

import random


class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):

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
        return "\n".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
        return hand


    def deal_hands(self, num_hands, num_cards_per_hand):
        new_hands = []
        for i in range(num_hands):
            hand_name = "hand " + str(i)
            h = Hand(hand_name)
            new_hands.append(self.move_cards(h, num_cards_per_hand))
            print h, "\n"
        return new_hands


class Hand(Deck):
    def __init__(self, label=""):
        self.cards = []
        self.label = label

hand = Hand('new hand')

print hand.cards

deck1 = Deck()
card = deck1.pop_card()
hand.add_card(card)

new_hands = deck1.deal_hands(5, 3)

for item in new_hands:
    print str(item), "\n"

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

print find_defining_class(hand, 'pop_card')