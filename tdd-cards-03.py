"""
V1. Create a function that can output a list of 52 cards in a deck.
V2. Display a list of 52 card names. "Ace of Hearts" through "King of Clubs"
V3. A card can be dealt from a deck into a hand.
"""


# LETS LEAVE THIS WORKING CODE ALONE FOR NOW
def list_cards():
    output = []
    for suit in range(0, 4):
        for value in range(0, 13):
            output.append((suit, value))
    return output


def card_names():
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    name_list = ["Ace"] + list(range(2, 11)) + ["Jack", "Queen", "King"]
    return list(map(lambda card: f"{name_list[card[1]]} of {suits[card[0]]}", list_cards()))


def deal_hand(cards: list, number: int = 5):
    return list(map(lambda i: cards.pop(), range(0, number)))


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
