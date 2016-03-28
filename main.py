from kivy.app import App
from kivy.graphics import BorderImage
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

spacing = 15


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
