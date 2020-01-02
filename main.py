from colorama import init, Fore, Style
init()

class TreeError(Exception):
    pass

class Lights():
    # Create separate class for this
    colors = {
        'R': {
            'color': Fore.RED,
            'repl': '●'
        },
        'G': {
            'color': Fore.GREEN,
            'repl': '●'
        },
        'B': {
            'color': Fore.BLUE,
            'repl': '●'
        },
        'Y': {
            'color': Fore.YELLOW,
            'repl': '*'
        } 
    }
    reset = Style.RESET_ALL

    def color(self, char: str) -> str:
        if clr := self.colors.get(char):
            return f'{clr["color"]}{clr["repl"]}'
        else:
            return f'{self.reset}{char}'

    def color_generator(self, chars: list) -> str:
        for char in chars:
            if clr := self.colors.get(char):
                yield f'{clr["color"]}{clr["repl"]}'
            else:
                yield f'{self.reset}{char}'


class Tree():
    _tree_str = None

    def __init__(self, file_name: str, **kwargs):
        self.file_name = file_name

    def open_file(self) -> list:
        try:
            with open(self.file_name, 'r') as f:
                self._tree_str = f.read().rstrip()
        except (EnvironmentError, FileNotFoundError):
            self._tree_str = None
        if not self._tree_str:
            raise TreeError('Could not open file or the file is empty')
        return list(self._tree_str)


if __name__ == '__main__':
    tree_obj = Tree('christmas_tree.txt')
    lights_obj = Lights()
    chars = tree_obj.open_file()
    print(''.join(lights_obj.color_generator(chars)))
    