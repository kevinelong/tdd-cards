"""
V1. Create a function that can output a list of 52 cards in a deck.
V2. Display a list of 52 card names. "Ace of Hearts" through "King of Clubs"
V3. A card can be dealt from a deck into a hand.
"""

from tdd_cards_module import Deck


# LETS LEAVE THIS WORKING CODE ALONE FOR NOW
def list_cards():
    return Deck().cards


def card_names():
    return Deck().names()


def deal_hand():
    return Deck().deal_hand(number).names()


""" TESTS """
if __name__ == "__main__":
    # V1 TESTS
    print("list_cards" in globals(), "Is Defined")
    print(52 == len(list_cards()), "Has 52 Cards")
    print(type(list_cards()) == list, "Is a List")

    # V2 TESTS
    print(52 == len(card_names()), "Has 52 Names")
    print(card_names()[0] == 'Ace of Hearts', "First card is the 'Ace of Hearts'")
    print(card_names()[-1] == 'King of Clubs', "Last card is the 'King of Clubs'")

    # V3 TESTS
    print(5 == len(deal_hand()), "Hand has five cards")
    print(deal_hand()[0] == 'King of Clubs', "First card is the 'King of Clubs'")
    print(deal_hand()[1] == 'Queen of Clubs', "Second card is the 'Queen of Clubs'")
