from dataclasses import dataclass

@dataclass
class Card:
    winning_numbers: [int]
    other_numbers: [int]
    card_point: int

    def __init__(self, line: str):
        self.winning_numbers = []
        self.other_numbers = []
        self.card_point = 0
        new_line = line.strip('\n')
        numbers = new_line.split(':')
        all_number = numbers[1]
        winning_numbers_string = all_number.split('|')[0]
        other_numbers_string = all_number.split('|')[1]
        winning_numbers_array = winning_numbers_string.split(' ')
        other_numbers_array = other_numbers_string.split(' ')
        for string in winning_numbers_array:
            if string.isdigit():
                self.winning_numbers.append(int(string))
        for string in other_numbers_array:
            if string.isdigit():
                self.other_numbers.append(int(string))

    def is_winning_number(self, number: int):
        if number in self.winning_numbers:
            return True
        else:
            return False

    def update_card_point(self, number):
        if self.is_winning_number(number):
            if self.card_point == 0:
                self.card_point = 1
            else:
                self.card_point = self.card_point * 2


@dataclass
class Cards:
    cards: [str]

    def __init__(self, file: str):
        with open(file) as f:
            self.cards = f.readlines()


def main():
    cards = Cards('text.txt').cards
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