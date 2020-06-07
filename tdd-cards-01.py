"""
V1. Create a function that can output a list of 52 cards in a deck.
"""


def list_cards():
    output = []
    for suit in range(0, 4):
        for value in range(0, 13):
            output.append((suit, value))
    return output


""" TESTS """
if __name__ == "__main__":
    # V1 TESTS
    print("list_cards" in globals(), "Is Defined")
    print(52 == len(list_cards()), "Has 52 Cards")
    print(type(list_cards()) == list, "Is a List")
