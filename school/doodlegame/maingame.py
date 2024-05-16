import arcade

SCREEN_TITLE = "Eraser Run"
CHARACTER_SCALING = 0.5
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
TILE_SCALING = 0.5
PLAYER_V = 5


class GameWindow(arcade.Window):

    def __init__(self, width, height, title):

        # Init the parent class
        super().__init__(width, height, title)
        self.wall_list = None
        self.player_list = None
        self.scene = None

        self.player_sprite = None

        self.physics_engine = None

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.scene = arcade.Scene()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls"))

        self.scene.add_sprite_list('Player')
        self.scene.add_sprite_list('Walls', use_spatial_hash=True)
        
        filelocation = 'C:/Users/ericl/Documents/lab/school/doodlegame/player_1/player_running.png'
        self.player_sprite = arcade.Sprite(filelocation, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 120
        self.player_list.append(self.player_sprite)
        self.scene.add_sprite('Player', self.player_sprite)

        for x in range(0, 1250, 64):
            wall = arcade.Sprite('C:/Users/ericl/Documents/lab/school/doodlegame/terrain/grass1.jpg', TILE_SCALING)
            wall.center_x = x
            wall.center_y = 10
            self.wall_list.append(wall)
            self.scene.add_sprite('Walls', wall)
        
        coordinates_list = [[512, 96], [256, 96], [768, 96]]
        for coord in coordinates_list:
            wall = arcade.Sprite('C:/Users/ericl/Documents/lab/school/doodlegame/terrain/cow1.png', TILE_SCALING)
            wall.position = coord
            self.scene.add_sprite('Walls', wall)

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_V
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_V
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_V
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_V

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()


def main():
    """ Main function """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()