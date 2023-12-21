from dataclasses import dataclass


def has_special_character(characters: [str]) -> bool:
    for character in characters:
        if character in Grid.CHARACTERS:
            return True
    return False

@dataclass
class Grid:
    CHARACTERS = "%$@&#/-+*="

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

    def get_characters_around(self, y: int, x: int) -> [str]:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1),
        ]
        characters = []
        for (d_y, d_x) in directions:
            characters.append(self.get_character(y + d_y, x + d_x))
        return characters

    def get_number(self, y: int, x: int) -> int:
        index = x
        number = []
        while self.is_digit(y, index):
            number.append(self.get_character(y, index))
            index = index + 1
        return int(''.join(number))


def main():
    grid = Grid('text.txt')

    numbers_list = []
    for index_y, line in enumerate(grid.map):
        for index_x, _ in enumerate(line):
            if grid.is_digit(index_y, index_x) and not grid.is_digit(index_y, index_x - 1):
                number = grid.get_number(index_y, index_x)
                number_length = len(str(number))
                for i, index in enumerate(range(number_length)):
                    character_around = grid.get_characters_around(index_y, index_x + i)
                    if has_special_character(character_around):
                        numbers_list.append(number)
                        break
    numbers_sum = sum(numbers_list)
    print(numbers_sum)


if __name__ == '__main__':
    main()
