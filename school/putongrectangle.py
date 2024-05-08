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
arcade.set_background_color(arcade.color.ASH_GREY)

# Clear screen and start render process
arcade.start_render()

# --- Drawing Commands Will Go Here ---

# Draw the face
x = 300
y = 500
width = 100
height = 120
arcade.draw_ellipse_outline(x, y, width, height, arcade.color.GHOST_WHITE, 2)

# Draw the shaft
start_x = 300
start_y = 442
end_x = 300
end_y = 320
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.GHOST_WHITE, 2)

start_x = 300
end_x = 300
start_y = 410
end_y = 400
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 1)

start_x = 301
end_x = 301
start_y = 405
end_y = 395
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 1)

start_x = 300
end_x = 300
start_y = 360
end_y = 350
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 1)

start_x = 301
end_x = 301
start_y = 355
end_y = 345
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 1)

# Draw the handle
firstpoint = (300, 325)
secondpoint = (295, 308)
lastpoint = (305, 308)
polygon = [firstpoint, secondpoint, lastpoint]
arcade.draw_polygon_filled(polygon, arcade.color.YELLOW)

start_x = 300
start_y = 308
end_x = 300
end_y = 240
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.YELLOW, 10)

start_x = 300
start_y = 240
end_x = 300
end_y = 246
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.YELLOW, 12)

# Draw strings
start_y = 560
start_x = 250
end_x = 250
end_y = 442
while start_x < 350:
    arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.GHOST_WHITE, 1)
    start_x += 3
    end_x += 3

start_y = 450
start_x = 260
end_x = 340
end_y = 450
while start_y < 550:
    arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.GHOST_WHITE, 1)
    start_y += 3
    end_y += 3

# Finish head
arcade.draw_text('(', 220, 450, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text(')', 318, 450, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('v', 180, 470, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('v', 328, 470, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('>', 200, 378, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('<', 300, 378, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('<', 300, 513, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('>', 200, 513, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('^', 317, 380, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')
arcade.draw_text('^', 183, 380, arcade.color.ASH_GREY, 150, 19, 'left', 'calibri')

arcade.draw_arc_outline(300, 500, 100, 120, arcade.color.BLACK, 340, 435, 3)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()