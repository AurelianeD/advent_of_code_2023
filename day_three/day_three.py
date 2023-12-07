from dataclasses import dataclass

@dataclass
class Grid:
    x: str
    y: str
    x_index: int
    y_index: int

    def is_digit(self):
        print(self.character.is_digit())

@dataclass
class Text:
    path: str
    lines: list
    text_content: str = ''

    def read_file(self):
        with open(self.path) as file:
            for line in file:
                self.lines.append(line)

def main():
    text = Text('text.txt', [])
    text.read_file()
    print(text.lines[0])

if __name__ == '__main__':
    main()
