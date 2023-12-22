from dataclasses import dataclass


def has_special_character(characters: [str]) -> bool:
    for character in characters:
        if character in Grid.CHARACTERS:
            return True
    return False



@dataclass
class Grid:
    CHARACTERS = "%$@&#/-+*="
    DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1),
    ]

    map: [str]

    def __init__(self, file: str):
        with open(file) as f:
            self.map = f.readlines()

    def get_character(self, y: int, x: int) -> str:
        if y == -1 or x == -1:
            return '.'
        try:
            return self.map[y][x]
        except IndexError:
            return '.'

    def is_digit(self, y: int, x: int) -> bool:
        return self.get_character(y, x).isdigit()

    def is_start(self, y: int, x: int) -> bool:
        return self.get_character(y, x) == '*'

    def get_characters_around(self, y: int, x: int) -> [str]:

        characters = []
        for (d_y, d_x) in self.DIRECTIONS:
            characters.append(self.get_character(y + d_y, x + d_x))
        return characters

    def get_numbers_around(self, y: int, x: int) -> [int]:
        numbers = []
        for (d_y, d_x) in self.DIRECTIONS:
            is_digit = self.is_digit(d_y + y, d_x + x)
            if is_digit:
                number_first_index = self.get_first_character_number_index(d_y + y, d_x + x)
                number = self.get_number(d_y + y, number_first_index)
                if number not in numbers:
                    numbers.append(number)
        return numbers

    def get_number(self, y: int, x: int) -> int:
        index = x
        number = []
        while self.is_digit(y, index):
            number.append(self.get_character(y, index))
            index = index + 1
        return int(''.join(number))

    def get_first_character_number_index(self, y: int, x: int) -> int:
        index = x
        while self.is_digit(y, index):
            index = index - 1
        return index + 1


def main():
    grid = Grid('text.txt')
    # grid = Grid('subject.txt')

    numbers_list_one = []
    numbers_list_two = []

    def part_one(y: int, x: int):
        if grid.is_digit(y, x) and not grid.is_digit(y, x - 1):
            number = grid.get_number(y, x)
            number_length = len(str(number))
            for i, index in enumerate(range(number_length)):
                character_around = grid.get_characters_around(y, x + i)
                if has_special_character(character_around):
                    numbers_list_one.append(number)
                    break

    def part_two(y: int, x: int):
        if grid.is_start(y, x):
            numbers_around = grid.get_numbers_around(y,x)
            if len(numbers_around) == 2:
                numbers_list_two.append(numbers_around[0] * numbers_around[1])

    for index_y, line in enumerate(grid.map):
        for index_x, _ in enumerate(line):
            part_one(index_y, index_x)
            part_two(index_y, index_x)
    part_one_response = sum(numbers_list_one)
    part_two_response = sum(numbers_list_two)
    print('Part one response:', part_one_response)
    print('Part two response:', part_two_response)


if __name__ == '__main__':
    main()
