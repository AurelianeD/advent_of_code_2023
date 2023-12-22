from dataclasses import dataclass


def get_value(line: str) -> [int]:
    numbers = []
    new_line = line.strip('\n')
    array = new_line.split(' ')
    for i in array:
        if i.isdigit():
            numbers.append(int(i))
    return numbers


def calculate_distance(speed: int)


def numbers_of_different_ways(milliseconds: int, max_distance: int) -> [int]:
    numbers = []
    for millisecond in range(0, milliseconds + 1):
        time_holding_button = millisecond

@dataclass
class Game:
    map: [str]

    def __init__(self, file: str):
        with open(file) as f:
            self.map = f.readlines()

def main():
    game = Game('text.txt')
    times = get_value(game.map[0])
    distances = get_value(game.map[1])
    print(numbers_of_different_ways(times[0], distances[0]))
    print(distances)

    pass


if __name__ == '__main__':
    main()