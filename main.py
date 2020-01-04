from colorama import init, Fore, Style
init()

class TreeError(Exception):
    pass

class Light():

    def __init__(self, replace_char: str, color_char: str, color: Fore):
        self.replace_char = replace_char
        self.color = color
        self.color_char = color_char

class LightsDriver():
    colors = {}
    reset = Style.RESET_ALL

    def color(self, char: str) -> str:
        if clr := self.colors.get(char):
            return f'{clr["color"]}{clr["repl"]}'
        else:
            return f'{self.reset}{char}'

    def color_generator(self, chars: list) -> str:
        for char in chars:
            if light := self.colors.get(char):
                yield f'{light.color}{light.replace_char}'
            else:
                yield f'{self.reset}{char}'

    def add_light(self, light_obj: Light):
        self.colors.setdefault(light_obj.color_char, light_obj)


class Tree():
    _tree_str = None

    def __init__(self, file_name: str):
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
    lights_obj = LightsDriver()
    chars = tree_obj.open_file()
    wanted_colors = (('R', '●', Fore.RED), ('G', '●', Fore.GREEN), ('B', '●', Fore.BLUE), ('Y', '⋆', Fore.YELLOW))
    for item in wanted_colors:
        color_char, replace_char, color = item
        lights_obj.add_light(Light(replace_char, color_char, color))
    print(''.join(lights_obj.color_generator(chars)))
    