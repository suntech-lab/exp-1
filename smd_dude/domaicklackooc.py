import arcade

# Set constants for the screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Penguin Picture"

# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.AZURE)

# Clear screen and start render process
arcade.start_render()

# Function to draw a block of ice
def draw_ice_block(x, y, width, height):
    arcade.draw_rectangle_filled(x, y, width, height, arcade.color.LIGHT_CYAN)
    arcade.draw_rectangle_outline(x, y, width, height, arcade.color.BLUE_GRAY, 2)

# Function to draw an igloo
def draw_igloo(x, y):
    # Igloo base
    arcade.draw_arc_filled(x, y, 150, 100, arcade.color.WHITE, 0, 180)
    arcade.draw_arc_outline(x, y, 150, 100, arcade.color.BLACK, 0, 180, 2)

    # Igloo entrance
    arcade.draw_rectangle_filled(x, y - 40, 40, 40, arcade.color.BLACK)
    arcade.draw_rectangle_outline(x, y - 40, 40, 40, arcade.color.BLACK, 2)

# Function to draw a simple penguin
def draw_penguin(x, y):
    # Body
    arcade.draw_ellipse_filled(x, y, 50, 70, arcade.color.BLACK)
    arcade.draw_ellipse_filled(x, y - 10, 40, 50, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 10, y + 20, 5, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 10, y + 20, 5, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 10, y + 20, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 10, y + 20, 2, arcade.color.BLACK)

    # Beak
    arcade.draw_triangle_filled(x, y + 10, x - 5, y, x + 5, y, arcade.color.ORANGE)

    # Feet
    arcade.draw_triangle_filled(x - 15, y - 35, x - 5, y - 45, x - 25, y - 45, arcade.color.ORANGE)
    arcade.draw_triangle_filled(x + 15, y - 35, x + 5, y - 45, x + 25, y - 45, arcade.color.ORANGE)

# Function to draw a cloud
def draw_cloud(x, y):
    arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 40, y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 80, y, 40, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 20, y - 20, 30, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 60, y - 20, 30, arcade.color.WHITE)

# Draw sea and ice blocks
arcade.draw_rectangle_filled(500, 300, 1000, 600, arcade.color.LIGHT_BLUE)

# Draw ice blocks
draw_ice_block(300, 300, 200, 100)
draw_ice_block(700, 300, 200, 100)

# Draw igloo
draw_igloo(300, 350)

# Draw penguin
draw_penguin(700, 350)

# Draw clouds
draw_cloud(200, 800)
draw_cloud(700, 900)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()