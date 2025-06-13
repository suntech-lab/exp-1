import arcade
import time

SCREEN_TITLE = "Eraser Run"
CHARACTER_SCALING = 0.5
COIN_SCALING = 0.1
SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 700
TILE_SCALING = 0.5
PLAYER_V = 10 #speed of player
GRAVITY = 1
PLAYER_JUMP_V = 30 #speed of player's jump
PLAYER_START_X = 500
PLAYER_START_Y = 120
PLATFORMLAYERNAME = 'Platforms' #the name of the layer in the Tiled file that holds the platforms
COINLAYERNAME = 'Coins' #name of layer that holds coins
CAMERA_SPEED = 3 #speed of the camera pan
UPDATES = 60 #updates per second


class GameWindow(arcade.Window): #creating class for the game window

    def __init__(self, width, height, title):

        # Init the parent class
        super().__init__(width, height, title)
        self.eraser_list = arcade.SpriteList()
        self.scene = None
        self.camera = None
        self.window_center = None
        self.screen_x = -50
        self.screen_y = None
        self.tick_counter = 0

        self.player_sprite = None
        self.eraser_sprite = None
        self.crayon_sprite = None
        self.whiteblock = None

        self.physics_engine = None

        #loading game sounds
        self.collect_coin_sound = arcade.load_sound('C:/Users/ericl/Documents/lab/school/doodlegame/terrain/crayoncollectsound.mp3')
        self.jump_sound = arcade.load_sound('C:/Users/ericl/Documents/lab/school/doodlegame/player_1/playerjumpsound.mp3')

        self.gui_camera = None
        self.crayon_health = 10
        self.eraser_health = 100

        self.tile_map = None

        #scheduling game updates
        arcade.schedule(self.on_update, 1/UPDATES)

        #setting background colour
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):

        #setting up camera and initial health values for crayon and eraser
        self.camera = arcade.Camera(self.width, self.height)    
        self.gui_camera = arcade.Camera(self.width, self.height)
        self.crayon_health = 10
        self.eraser_health = 100

        #loading map from files
        map_name = 'C:/Users/ericl/Documents/lab/school/doodlegame/terrain/map1.tmx'
        layer_options = {'Platforms': {'use_spatial_hash': True}}
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        #loading the sprite of the player, putting it in position
        filelocation = 'C:/Users/ericl/Documents/lab/school/doodlegame'
        self.player_sprite = arcade.Sprite(filelocation + '/player_1/player_running.png', CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite('Player', self.player_sprite)

        #loading eraser and crayon sprites, putting crayon in position
        self.eraser_sprite = arcade.Sprite(filelocation + '/terrain/eraser.png', CHARACTER_SCALING)
        self.crayon_sprite = arcade.Sprite(filelocation + '/terrain/crayon.png', 1)
        self.whiteblock = arcade.Sprite(filelocation + '/terrain/whiteblock.png', 3)
        self.whiteblock.center_x = 1300
        self.crayon_sprite.center_x = 1300

        #setting background colour if available
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        #setting up physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=[self.scene[PLATFORMLAYERNAME]] #gravity included
            )

    #drawing function for game window 
    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        self.eraser_sprite.draw()
        self.whiteblock.draw()
        self.crayon_sprite.draw()
        self.gui_camera.use()

        #drawing the health values on screen
        crayon_health = (f'CRAYON HEALTH !!! : {self.crayon_health}')
        arcade.draw_text(crayon_health, 10, 450, arcade.csscolor.BLACK, 18)
        eraser_health = (f'ERASER BAD GUY HEALTH !!! {self.eraser_health}')
        arcade.draw_text(eraser_health, 10, 500, arcade.csscolor.BLACK, 18)

    #handling key press events
    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_V
                arcade.play_sound(self.jump_sound) #plays the sound when jumping
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_V
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_V
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_V

    #handling key release events
    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    #setting up the camera, centering it to the player except for the lower boundry and the x axis
    def center_camera(self):
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height/2)

        if screen_center_y < 0:
            screen_center_y = 0

        self.screen_x += CAMERA_SPEED

        window_center = self.screen_x, screen_center_y

        self.camera.move_to(window_center)

    #function for game updates
    def on_update(self, delta_time):
        self.physics_engine.update()

        if self.tick_counter == 200:
            self.crayon_health -= 1
        
        if self.tick_counter == 300:
            self.eraser_health -= 1
            self.tick_counter = 0
        self.tick_counter += 1

        #checking for coin collision, updating crayon health
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene['Coins'])
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.crayon_health += 1

        #eraser erases tiles it has come into contact with
        tile_hit_list = arcade.check_for_collision_with_list(self.eraser_sprite, self.scene['Platforms'])
        for platform in tile_hit_list:
            platform.remove_from_sprite_lists()

        #lose/win conditions
        if self.player_sprite.center_y < -10:
            exit()

        if self.player_sprite.center_x > self.crayon_sprite.center_x:
            time.sleep(1)
            exit()

        if self.crayon_health == 0:
            exit()

        if self.eraser_health == 0:
            exit()

        if arcade.check_for_collision(self.player_sprite, self.eraser_sprite) == True:
            exit()

        #moving the eraser and crayon sprites
        self.eraser_sprite.center_x += 3
        self.crayon_sprite.center_x += 3
        self.whiteblock.center_x += 3

        #vertical movement: eraser
        if self.eraser_sprite.center_y >= self.player_sprite.center_y + self.height:
            self.eraser_dir = 0
        if self.eraser_sprite.center_y <= 0:
            self.eraser_dir = 1
        if self.eraser_dir:
            self.eraser_sprite.center_y += 25
        else:
            self.eraser_sprite.center_y -= 25

        #vertical movement: crayon
        if self.crayon_sprite.center_y >= self.player_sprite.center_y + self.height:
            self.crayon_dir = 0
        if self.crayon_sprite.center_y <= 0:
            self.crayon_dir = 1
        if self.crayon_dir:
            self.crayon_sprite.center_y += 25
        else:
            self.crayon_sprite.center_y -= 25

        self.center_camera()

def main():
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()