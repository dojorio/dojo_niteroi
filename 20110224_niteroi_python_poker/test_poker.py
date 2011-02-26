import unittest
from poker import Card, Hand

class TestPoker(unittest.TestCase):

    def test_pair_6_at_first_and_second_position(self):
        card_list = [
            Card("H","6"), 
            Card("C","6"), 
            Card("H","8"), 
            Card("H","9"),
            Card("H","10"),
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "One Pair")

    def test_high_card_hand(self):
        card_list = [
            Card("H","6"), 
            Card("C","5"), 
            Card("H","8"), 
            Card("D","2"),
            Card("H","10"),
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "High Card")

    def test_pair_de_7_first_and_second_position(self):
        card_list = [
            Card("H","7"), 
            Card("C","7"), 
            Card("H","8"), 
            Card("H","9"),
            Card("H","10"),
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "One Pair")
    
    def test_pair_de_7_forth_and_fifth_position(self):
        card_list = [
            Card("H","9"), 
            Card("H","10"), 
            Card("H","8"), 
            Card("H","7"),
            Card("C","7"),
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "One Pair")
    
    def test_pair_de_7_na_second_and_fourth_position(self):
        card_list = [
            Card("H","9"), 
            Card("H","7"), 
            Card("H","8"), 
            Card("C","7"),
            Card("H","10"),
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "One Pair")

    def test_two_pairs_7_and_9_at_first_until_four_pos(self):
        card_list = [
            Card("H","7"), 
            Card("S","7"), 
            Card("H","9"), 
            Card("C","9"),
            Card("H","10"),
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "Two Pairs")

    def test_three_of_kind_of_7_first_until_third_pos(self):
        card_list = [
            Card("H","7"), 
            Card("D","7"), 
            Card("S","7"), 
            Card("C","9"),
            Card("H","10"),
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "Three of a kind")
    
    def test_three_of_kind_of_7_third_to_last_pos(self):
        card_list = [
            Card("C","9"),
            Card("H","10"),
            Card("H","7"), 
            Card("D","7"), 
            Card("S","7"), 
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "Three of a kind")

    def test_three_of_kind_of_8_third_to_last_pos(self):
        card_list = [
            Card("C","9"),
            Card("H","10"),
            Card("H","8"), 
            Card("D","8"), 
            Card("S","8"), 
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "Three of a kind")

    def test_four_of_8_second_to_last_pos(self):
        card_list = [
            Card("C","9"),
            Card("C","8"),
            Card("H","8"), 
            Card("D","8"), 
            Card("S","8"), 
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "Four of a kind")

    def test_full_house_of_8_and_9(self):
        card_list = [
            Card("C","9"),
            Card("H","9"),
            Card("H","8"), 
            Card("D","8"), 
            Card("S","8"), 
        ]
        hand = Hand(card_list)
        self.assertEqual(hand.result(), "Full house")


unittest.main()
