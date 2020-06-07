"""
V1. Create a function that can output a list of 52 cards in a deck.
V2. Display a list of 52 card names. "Ace of Hearts" through "King of Clubs"
V3. A card can be dealt from a deck into a hand.
"""
from unittest import TestCase
from tdd_cards_module import Deck

""" TESTS """


# V1 TESTS
class TestDeck(TestCase):
    # def setUp(self) -> None:
    #     self.deck = Deck()
    #     self.names = Deck().names()

    def test_cards(self):
        # V1 TESTS
        print("Deck" in globals(), "Is Defined")
        print(111 == len(Deck().cards), "Has 52 Cards")
        print(type(Deck().cards) == list, "Is a List")

    def test_names(self):
        # V2 TESTS
        print(52 == len(Deck().names()), "Has 52 Names")
        print(Deck().names()[0] == 'Ace of Hearts', "First card is the 'Ace of Hearts'")
        print(Deck().names()[-1] == 'King of Clubs', "Last card is the 'King of Clubs'")

    def test_hand(self):
        # V3 TESTS
        print(5 == len(Deck().deal_hand().cards), "Hand has five cards")
        print(Deck().deal_hand().cards[0] == 'King of Clubs', "First card is the 'King of Clubs'")
        print(Deck().deal_hand().cards[1] == 'Queen of Clubs', "Second card is the 'Queen of Clubs'")
