"""
V1. Create a function that can output a list of 52 cards in a deck.
V2. Display a list of 52 card names. "Ace of Hearts" through "King of Clubs"
"""


# LETS LEAVE THIS WORKING CODE ALONE FOR NOW
def list_cards():
    output = []
    for suit in range(0, 4):
        for value in range(0, 13):
            output.append((suit, value))
    return output


def card_names():
    return [
        'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts',
        '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts',
        'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
        'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds',
        '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds',
        'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds',
        'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades',
        '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades',
        'Jack of Spades', 'Queen of Spades', 'King of Spades',
        'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs',
        '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs',
        'Jack of Clubs', 'Queen of Clubs', 'King of Clubs'
    ]


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
