import arcade

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bouncing Rectangle Example"

# Rectangle info
RECT_WIDTH = 50
RECT_HEIGHT = 50
RECT_COLOR = arcade.color.DARK_BROWN

BACKGROUND_COLOR = arcade.color.ALMOND

# Constants for gravity and jump strength
GRAVITY = 0.5
JUMP_STRENGTH = 10


class Item:
    """ This class represents our rectangle """

    def __init__(self):

        # Set up attribute variables

        # Where we are
        self.center_x = 0
        self.center_y = 0

        # Where we are going
        self.change_x = 0
        self.change_y = 0

        # Variables for gravity and jumping
        self.is_jumping = False

    def update(self):
        # Apply gravity if not jumping
        if not self.is_jumping:
            self.change_y -= GRAVITY

        # Move the rectangle
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check if we need to bounce off floor
        if self.center_y < RECT_HEIGHT / 2:
            self.center_y = RECT_HEIGHT / 2
            self.change_y = 0
            self.is_jumping = False

        # Check if we need to bounce off ceiling
        if self.center_y > SCREEN_HEIGHT - RECT_HEIGHT / 2:
            self.center_y = SCREEN_HEIGHT - RECT_HEIGHT / 2
            self.change_y = 0

        # Check if we need to bounce off right wall
        if self.center_x > SCREEN_WIDTH - RECT_WIDTH / 2:
            self.center_x = SCREEN_WIDTH - RECT_WIDTH / 2
            self.change_x *= -1

        # Check if we need to bounce off left wall
        if self.center_x < RECT_WIDTH / 2:
            self.center_x = RECT_WIDTH / 2
            self.change_x *= -1

    def jump(self):
        if not self.is_jumping:
            self.change_y = JUMP_STRENGTH*GRAVITY
            self.is_jumping = True

    def draw(self):
        # Draw the rectangle
        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     RECT_WIDTH,
                                     RECT_HEIGHT,
                                     RECT_COLOR)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Create our rectangle
        self.item = Item()
        self.item.center_x = 200
        self.item.center_y = 300
        self.item.change_x = 0
        self.item.change_y = 0

        # Set background color
        self.background_color = BACKGROUND_COLOR

    def on_update(self, delta_time):
        # Move the rectangle
        self.item.update()

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()

        # Draw the rectangle
        self.item.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.SPACE:
            self.item.jump()
        elif key == arcade.key.LEFT:
            self.item.change_x = -2
        elif key == arcade.key.RIGHT:
            self.item.change_x = 2

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT and self.item.change_x < 0:
            self.item.change_x = 0
        elif key == arcade.key.RIGHT and self.item.change_x > 0:
            self.item.change_x = 0


def main():
    """ Main function """
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
