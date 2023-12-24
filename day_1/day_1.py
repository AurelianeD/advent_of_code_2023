from dataclasses import dataclass

CORRESPONDENCE = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


@dataclass
class Line:
    numbers_in_line: [int]
    calibration: int
    calibration_part_two: int

    def __init__(self, line: str):
        self.numbers_in_line = []
        self.calibration = 0
        for character in line:

            if character.isdigit():
                self.numbers_in_line.append(character)

    def get_calibration(self):
        calibration_number = self.numbers_in_line[0] + self.numbers_in_line[-1]
        self.calibration = int(calibration_number)

if __name__ == '__main__':

    with open("text.txt") as f:
        results = []
        for line in f:
            numbers = []
            text_line = Line(line)
            text_line.get_calibration()
            results.append(text_line.calibration)
        print(sum(results))
