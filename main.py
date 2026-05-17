import arcade
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Shooter"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.player_x = SCREEN_WIDTH / 2
        self.player_y = 50

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.CYAN)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 10


def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()