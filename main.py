import random
import sys
from tkinter.constants import CENTER

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
        self.player_speed = 0
        self.bullets = []
        self.enemies = []
        self.enemy_spawn_timer = 0
        self.score = 0
        self.lives = 5
        self.game_over = False


    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.player_x, self.player_y, 20, arcade.color.CYAN)

        for bullet in self.bullets:
            arcade.draw_circle_filled(bullet[0], bullet[1], 5, arcade.color.YELLOW)

        for enemy in self.enemies:
            arcade.draw_circle_filled(enemy[0], enemy[1], 15, arcade.color.RED)

        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)
        arcade.draw_text(f"Lives: {self.lives}", 10, SCREEN_HEIGHT - 60, arcade.color.RED, 16)

        if self.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH/2 - 120, SCREEN_HEIGHT/2, arcade.color.WHITE, 50)
            arcade.draw_text("Final Score: " + str(self.score), SCREEN_WIDTH/2 - 80, SCREEN_HEIGHT/2 - 60, arcade.color.YELLOW, 25)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_speed = -5
        elif key == arcade.key.RIGHT:
            self.player_speed = 5
        elif key == arcade.key.SPACE:
            self.bullets.append([self.player_x, self.player_y])

        if key == arcade.key.ESCAPE:
            arcade.exit()

        if key == arcade.key.R and self.game_over:
            self.__init__()

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_speed = 0

    def on_update(self, delta_time):
        if self.game_over:
            return

        if self.lives <= 0:
            self.game_over = True

        print(self.bullets)
        self.player_x += self.player_speed

        if self.player_x < 20:
            self.player_x = 20
        if self.player_x > SCREEN_WIDTH - 20:
            self.player_x = SCREEN_WIDTH - 20

        for bullet in self.bullets:
            bullet[1] += 5

        self.bullets = [b for b in self.bullets if b[1] < SCREEN_HEIGHT]

        self.enemy_spawn_timer += delta_time
        if self.enemy_spawn_timer > 1.5:
            x = random.randint(20, SCREEN_WIDTH - 20)
            self.enemies.append([x, SCREEN_HEIGHT])
            self.enemy_spawn_timer = 0

        for enemy in self.enemies:
            enemy[1] -= 3
            #self.enemies = [e for e in self.enemies if e[1] > 0]
        surviving_enemies = []
        for enemy in self.enemies:
            if enemy[1] > 0:
                surviving_enemies.append(enemy)
            else:
                self.lives -= 1
            self.enemies = surviving_enemies

        for bullet in self.bullets[:]:
            for enemy in self.enemies[:]:
                if abs(bullet[0]-enemy[0]) < 20 and abs(bullet[1] - enemy[1]) < 20:
                    self.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 1
                    break




def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()