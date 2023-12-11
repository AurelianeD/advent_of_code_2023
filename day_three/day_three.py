from dataclasses import dataclass


@dataclass
class Grid:
    CHARACTERS = "%$@&#/-+*="

    map: [str]

    def __init__(self, file: str):
        with open(file) as f:
            self.map = f.readlines()

    def get_character(self, y, x):
        try:
            return self.map[y][x]
        except IndexError:
            return '.'

    def is_digit(self, y: int, x: int):
        return self.get_character(y, x).isdigit()

    def get_characters_around(self, y: int, x: int) -> [str]:
        directions = [
            (-1, -1), (-1, 0),  (-1, 1),
            (0, -1),            (0, 1),
            (1, -1), (1, 0),    (1, 1),
        ]
        characters = []
        for (d_y, d_x) in directions:
            characters.append(self.get_character(y + d_y, x + d_x))
        return characters

    def has_special_character(self, characters: [str]) -> bool:
        for character in characters:
            if character in Grid.CHARACTERS:
                return True
        return False

    def get_number(self, y, x):
        index = x
        number = []
        while self.is_digit(y, index):
            number.append(self.get_character(y, index))
            index = index + 1
        return int(''.join(number))


def main():
    grid = Grid('text.txt')

    for y, line in enumerate(grid.map):
        for x, character in enumerate(line):
            numbers_list = []
            if grid.is_digit(y, x):
                pass



if __name__ == '__main__':
    main()