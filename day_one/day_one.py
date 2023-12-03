if __name__ == '__main__':

    correspondence = {
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

    with open("text.txt") as f:
        results = []
        for line in f:
            numbers = []
            for character in line:
                if character.isdigit():
                    numbers.append(character)
                # part two
                # for number, value in correspondence.items():
                    # if number.startswith(character):
            result = numbers[0] + numbers[-1]
            results.append(int(result))
        print(sum(results))