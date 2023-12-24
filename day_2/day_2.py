from dataclasses import dataclass

@dataclass
class Game:
    id: int
    red: int = 0
    blue: int = 0
    green: int = 0

def process_line(line):
    game_str, content_str = line.split(':')
    _, game_id = game_str.split()
    game = Game(int(game_id))
    game_items = content_str.strip().split(';')

    for item in game_items:
        color_items = item.split(',')
        for color_item in color_items:
            color_value, color_name = color_item.strip().split()
            color_value = int(color_value)
            match color_name:
                case "red" if color_value > game.red:
                    game.red = color_value
                case "blue" if color_value > game.blue:
                    game.blue = color_value
                case "green" if color_value > game.green:
                    game.green = color_value
    return game

def main():
    possible_games = []
    product_game = []

    with open("text.txt") as f:
        for line in f:
            game = process_line(line)

            if game.red <= 12 and game.blue <= 14 and game.green <= 13:
                possible_games.append(game.id)

            product_colors = game.green * game.red * game.blue
            product_game.append(product_colors)

    print(sum(possible_games))
    print(sum(product_game))

if __name__ == '__main__':
    main()


