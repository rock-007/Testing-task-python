from src.card_game import CardGame
from src.card import Card
import unittest

class card_gameTest(unittest.TestCase):

    def setUp(self):
        self.cardGame = CardGame()
        self.first_card = Card("ace",1)
        self.second_card = Card("clubs",3)
        self.cards = [self.first_card, self.second_card]

def test_check_for_ace(self):
    self.assertEqual("Ace", self.cardGame.check_for_ace(self.first_card))

def test_highest_card(self):
    self.assertEqual(self.first_card, self.cardGame.higest_card(self.first_card, self.second_card))


def test_cards_total(self):
    self.assertEqual(4, self.cardGame.higest_card(self.cards))

