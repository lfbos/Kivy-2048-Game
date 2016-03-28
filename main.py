from kivy.app import App
from kivy.graphics import BorderImage
from kivy.uix.widget import Widget

spacing = 15


class Board(Widget):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.resize()

    def resize(self):
        self.cell_size = (0.25 * (self.width - 5 * spacing),) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos=self.pos, size=self.size, source='board.png')

    on_pos = resize
    on_size = resize


class GameApp(App):
    pass


if __name__ == '__main__':
    GameApp().run()
