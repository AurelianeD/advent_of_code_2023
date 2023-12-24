from dataclasses import dataclass


def get_values(line: str) -> [int]:
    numbers = []
    new_line = line.strip('\n')
    array = new_line.split(' ')
    for i in array:
        if i.isdigit():
            numbers.append(int(i))
    return numbers


def get_value(line: str) -> int:
    number = ''
    new_line = line.strip('\n')
    array = new_line.split(' ')
    for i in array:
        if i.isdigit():
            number = number + i
    return int(number)


def calculate_distance(time: int, max_time: int) -> int:
    return time * (max_time - time)


def numbers_of_different_ways(milliseconds: int, max_distance: int) -> [int]:
    numbers = 0
    for millisecond in range(0, milliseconds + 1):
        time_holding_button = millisecond
        distance = calculate_distance(time_holding_button, milliseconds)
        if distance > max_distance:
            numbers = numbers + 1
    return numbers


@dataclass
class Game:
    map: [str]

    def __init__(self, file: str):
        with open(file) as f:
            self.map = f.readlines()


def main():
    game = Game('text.txt')
    # game = Game('subject.txt')
    times = get_values(game.map[0])
    distances = get_values(game.map[1])

    time = get_value(game.map[0])
    distance = get_value(game.map[1])

    round_one = numbers_of_different_ways(times[0], distances[0])
    round_two = numbers_of_different_ways(times[1], distances[1])
    round_three = numbers_of_different_ways(times[2], distances[2])
    round_four = numbers_of_different_ways(times[3], distances[3])

    result_part_one = round_one * round_two * round_three * round_four
    result_part_two = numbers_of_different_ways(time, distance)

    print(result_part_one)
    print(result_part_two)


if __name__ == '__main__':
    main()
