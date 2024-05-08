"""
Drawing an example happy face

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.happy_face
"""

import arcade

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Badminton Racquet"

# Open the window. Set the window title and dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.WHITE)

# Clear screen and start render process
arcade.start_render()

# --- Drawing Commands Will Go Here ---

# Draw the face
x = 300
y = 500
width = 100
height = 120
arcade.draw_ellipse_outline(x, y, width, height, arcade.color.BLACK, 2)

# Draw the shaft
start_x = 300
start_y = 442
end_x = 300
end_y = 320
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 2)

# Draw the handle
firstpoint = (300, 325)
secondpoint = (295, 308)
lastpoint = (305, 308)
polygon = [firstpoint, secondpoint, lastpoint]
arcade.draw_polygon_filled(polygon, arcade.color.BLACK)

start_x = 300
start_y = 308
end_x = 300
end_y = 240
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 10)

start_x = 300
start_y = 240
end_x = 300
end_y = 246
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 12)

# Draw strings

start_y = 560
start_x = 250
end_x = 250
end_y = 442
while start_x < 350:
    arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 1)
    start_x += 2
    end_x += 2

arcade.draw

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()