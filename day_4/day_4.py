from dataclasses import dataclass


@dataclass
class Card:
    winning_numbers: [int]
    other_numbers: [int]
    card_point: int
    line: str

    def __init__(self, line: str):
        self.winning_numbers = []
        self.other_numbers = []
        self.card_point = 0
        self.line = line

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


def main():
    with open('text.txt') as f:
        cards = f.readlines()
        cards_point = 0

        for line in cards:
            card = Card(line)
            other_numbers = card.other_numbers
            for number in other_numbers:
                card.update_card_point(number)
            cards_point = cards_point + card.card_point

        print(cards_point)


if __name__ == '__main__':
    main()
