class Card():

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, another):
        return self.suit == another.suit and self.value == another.value

class Hand():

    def __init__(self, cards):
        self.cards = cards

    def result(self):

        if self.is_full_house():
            return "Full house"
        if self.is_three_of_a_kind():
            return "Three of a kind"  
        if self.is_two_pairs():
            return "Two Pairs"
        if self.is_one_pair():
            return "One Pair" 
        if self.is_four_of_a_kind():
            return "Four of a kind"

        return "High Card"

    def is_one_pair(self):
        values = [carta.value for carta in self.cards ]

        for value in values:
            if values.count(value) == 2:
                return True

        return False

    def is_full_house(self):
        return self.is_one_pair() and self.is_three_of_a_kind()

    def is_two_pairs(self):
        values_set = set([carta.value for carta in self.cards])

        if len(values_set) == 3:
            return True

        return False

    def is_three_of_a_kind(self):
        values = [carta.value for carta in self.cards ]

        for value in values:
            if values.count(value) == 3:
                return True

        return False

    def is_four_of_a_kind(self):
        values_set = set([carta.value for carta in self.cards])

        if len(values_set) == 2:
            return True

        return False
