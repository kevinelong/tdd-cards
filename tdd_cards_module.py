from dataclasses import dataclass

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
name_list = ["Ace"] + list(range(2, 11)) + ["Jack", "Queen", "King"]


@dataclass
class Card:
    suit: int
    value: int

    def name(self):
        return f"{name_list[self.value]} of {suits[self.suit]}"


@dataclass
class CardContainer:
    cards: list

    def names(self):
        return list(map(lambda card: card.name(), self.cards))


class Hand(CardContainer):
    pass


@dataclass
class Deck(CardContainer):

    def __init__(self):
        self.cards = []
        for suit in range(0, 4):
            for value in range(0, 13):
                self.cards.append(Card(suit, value))

    def deal_card(self):
        return self.cards.pop()

    def deal_hand(self, number: int = 5):
        return Hand(list(map(lambda i: self.deal_card(), range(0, number))))


if __name__ == "__main__":
    deck = Deck()
    print(deck.names())
