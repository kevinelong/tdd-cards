"""
V1. Create a function that can output a list of 52 cards in a deck.
V2. Display a list of 52 card names. "Ace of Hearts" through "King of Clubs"
V3. A card can be dealt from a deck into a hand.
"""
from unittest import TestCase, main
from tdd_cards_module05 import Deck

""" TESTS """


# V1 TESTS
class TestDeck(TestCase):
    # def setUp(self) -> None:
    #     self.deck = Deck()
    #     self.names = Deck().names()

    def test_cards(self):
        # V1 TESTS
        self.assertTrue("Deck" in globals(), "Is Defined")
        self.assertTrue(52 == len(Deck().cards), "Has 52 Cards")
        self.assertTrue(type(Deck().cards) == list, "Is a List")

    def test_names(self):
        # V2 TESTS
        self.assertTrue(52 == len(Deck().names()), "Has 52 Names")
        self.assertTrue(Deck().names()[0] == 'Ace of Hearts', "First card is the 'Ace of Hearts'")
        self.assertTrue(Deck().names()[-1] == 'King of Clubs', "Last card is the 'King of Clubs'")

    def test_hand(self):
        # V3 TESTS
        self.assertTrue(5 == len(Deck().deal_hand().cards), "Hand has five cards")
        self.assertTrue(Deck().deal_hand().names()[0] == 'King of Clubs', "First card is the 'King of Clubs'")
        self.assertTrue(Deck().deal_hand().names()[1] == 'Queen of Clubs', "Second card is the 'Queen of Clubs'")


if __name__ == "__main__":
    main()
