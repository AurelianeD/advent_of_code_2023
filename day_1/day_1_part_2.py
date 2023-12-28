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

INVERSE_CORRESPONDENCE = {
    "eno": 1,
    "owt": 2,
    "eerht": 3,
    "ruof": 4,
    "evif": 5,
    "xis": 6,
    "neves": 7,
    "thgie": 8,
    "enin": 9
}


def get_number(line: str):
    line = line.strip()

    first_digit = get_first_digit(line, CORRESPONDENCE)
    last_digit = get_first_digit(line[::-1], INVERSE_CORRESPONDENCE)

    return int(f'{first_digit}{last_digit}')


def get_first_digit(line: str, correspondence: dict[str, int]) -> int:
    for i in range(0, len(line)):
        line_character = line[i]
        if line_character.isdigit():
            return int(line_character)
        else:
            for digit_literal in correspondence.keys():
                for j in range(0, len(digit_literal)):
                    if i+j >= len(line) or line[i + j] != digit_literal[j]:
                        break
                    elif j == len(digit_literal) - 1:
                        return correspondence[digit_literal]

    return -1


def main():
    with open('text.txt') as f:
        result_sum = 0
        for line in f:
            number = get_number(line)
            print(number)
            result_sum += number
        print(result_sum)


if __name__ == '__main__':
    main()