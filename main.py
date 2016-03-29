from kivy.app import App
from kivy.graphics import BorderImage
from kivy.graphics import Color
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

spacing = 15

colors = (
    'EEE4DA', 'EDE0C8', 'F2B179', 'F59563',
    'F67C5F', 'F65E3B', 'EDCF72', 'EDCC61',
    'EDC850', 'EDC53F', 'EDC22E'
)

tile_colors = {2 ** i: color for i, color in enumerate(colors, start=1)}


class Tile(Widget):
    font_size = NumericProperty(24)
    number = NumericProperty(2)  # Text shown on the tile
    color = ListProperty(get_color_from_hex(tile_colors[2]))
    number_color = ListProperty(get_color_from_hex('776E65'))

    def __init__(self, number=2, **kwargs):
        super(Tile, self).__init__(**kwargs)
        self.font_size = 0.5 * self.width
        self.number = number
        self.update_colors()

    def update_colors(self):
        self.color = get_color_from_hex(tile_colors[self.number])
        if self.number > 4:
            self.number_color = get_color_from_hex('F9F6F2')

    def resize(self, pos, size):
        self.pos = pos
        self.size = size
        self.font_size = 0.5 * self.width


def all_cells():
    for x in range(4):
        for y in range(4):
            yield (x, y)


class Board(Widget):
    b = None

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.resize()

    def reset(self):
        self.b = [[None for i in range(4)]
                  for j in range(4)]

    def cell_pos(self, board_x, board_y):
        return (self.x + board_x * (self.cell_size[0] + spacing) + spacing,
                self.y + board_y * (self.cell_size[1] + spacing) + spacing)

    def resize(self, *args):
        self.cell_size = (0.25 * (self.width - 5 * spacing),) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos=self.pos, size=self.size, source='board.png')
            Color(*get_color_from_hex('CCC0B4'))
            for board_x, board_y in all_cells():
                BorderImage(
                    pos=self.cell_pos(board_x, board_y),
                    size=self.cell_size,
                    source='cell.png'
                )

        if not self.b:
            return

        for board_x, board_y in all_cells():
            tile = self.b[board_x][board_y]
            if tile:
                tile.resize(
                    pos=self.cell_pos(board_x, board_y),
                    size=self.cell_size
                )

    def valid_cell(self, board_x, board_y):
        return (0 <= board_x <= 3 and 0 <= board_y <= 3)

    def can_move(self, board_x, board_y):
        return (self.valid_cell(board_x, board_y) and
                self.b[board_x][board_y] is None)

    on_pos = resize
    on_size = resize


class GameApp(App):
    def on_start(self):
        board = self.root.ids.board
        board.reset()


if __name__ == '__main__':
    GameApp().run()
