from dataclasses import dataclass


@dataclass
class Card:
    winning_numbers: [int]
    other_numbers: [int]
    card_point: int
    line: str
    copies: int
    matching_numbers: int

    def __init__(self, line: str):
        self.winning_numbers = []
        self.other_numbers = []
        self.card_point = 0
        self.line = line
        self.copies = 1
        self.matching_numbers = 0

        self.compute()

    def parse(self):
        card, all_number = self.line.strip('\n').split(':')
        return [number_list.split(' ') for number_list in all_number.split('|')]

    def compute(self):
        winning_numbers_array, other_numbers_array = self.parse()
        for array, list_to_add in ((winning_numbers_array, self.winning_numbers), (other_numbers_array, self.other_numbers)):
            for string in array:
                if string.isdigit():
                    list_to_add.append(int(string))

    def is_winning_number(self, number: int):
        return number in self.winning_numbers

    def update_card_point(self, number):
        if self.is_winning_number(number):
            if self.card_point == 0:
                self.card_point = 1
            else:
                self.card_point = self.card_point * 2

    def compute_matching_numbers(self, number):
        if self.is_winning_number(number):
            self.matching_numbers += 1

    def add_copy(self):
        self.copies += 1


@dataclass
class Cards:
    cards: [Card]

    def __init__(self, lines: [str]):
        self.cards = []
        for line in lines:
            self.cards.append(Card(line))

    def sum_cards_point(self) -> int:
        return sum(c.card_point for c in self.cards)

    def sum_cards_copies(self) -> int:
        return sum(c.copies for c in self.cards)


def main():
    with open('text.txt') as f:
        lines = f.readlines()
        cards = Cards(lines)

        for index, card in enumerate(cards.cards):
            increment = 0
            other_numbers = card.other_numbers
            for number in other_numbers:
                card.update_card_point(number)
                card.compute_matching_numbers(number)
            while increment < card.copies:
                for i in range(card.matching_numbers):
                    cards.cards[index + i + 1].add_copy()
                increment += 1

        print('result part 1 :', cards.sum_cards_point())
        print('result part 2 :', cards.sum_cards_copies())


if __name__ == '__main__':
    main()
