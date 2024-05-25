import arcade
import random

SCREEN_TITLE = "Eraser Run"
CHARACTER_SCALING = 0.5
COIN_SCALING = 0.1
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
TILE_SCALING = 0.5
PLAYER_V = 10
GRAVITY = 1
PLAYER_JUMP_V = 30
PLAYER_START_X = 64
PLAYER_START_Y = 120
PLATFORMLAYERNAME = 'Platforms'
COINLAYERNAME = 'Coins'
DEATHLAYERNAME = 'Deadspace'

class GameWindow(arcade.Window):

    def __init__(self, width, height, title):

        # Init the parent class
        super().__init__(width, height, title)
        self.wall_list = None
        self.player_list = None
        self.scene = None
        self.camera = None

        self.player_sprite = None

        self.physics_engine = None

        self.collect_coin_sound = arcade.load_sound('C:/Users/ericl/Documents/lab/school/doodlegame/terrain/crayoncollectsound.mp3')
        self.jump_sound = arcade.load_sound('C:/Users/ericl/Documents/lab/school/doodlegame/player_1/playerjumpsound.mp3')

        self.gui_camera = None
        self.score = 0

        self.tile_map = None

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)
        self.score = 0
        
        map_name = 'C:/Users/ericl/Documents/lab/school/doodlegame/terrain/map1.tmx'
        layer_options = {'Platforms': {'use_spatial_hash': True}}
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        filelocation = 'C:/Users/ericl/Documents/lab/school/doodlegame/player_1/player_running.png'
        self.player_sprite = arcade.Sprite(filelocation, CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite('Player', self.player_sprite)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=[self.scene["Platforms"],self.scene['Deadspace']]
            )

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        self.gui_camera.use()

        score_text = (f'SCORE : {self.score}')
        arcade.draw_text(score_text, 10, 450, arcade.csscolor.BLACK, 18)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_V
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_V
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_V
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_V

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width/2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height/2)

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene['Coins'])
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1

        if self.player_sprite.center_y < -10:
            exit()
        if arcade.check_for_collision_with_list(self.player_sprite, self.scene['Deadspace']):
            exit()
        else:
            pass

        self.center_camera_to_player()

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()