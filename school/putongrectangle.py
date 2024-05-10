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
arcade.set_background_color(arcade.color.BALL_BLUE)

# Clear screen and start render process
arcade.start_render()

# --- Drawing Commands Will Go Here ---

# Draw background
center_x = 300
center_y = 100
width = 600
height = 250
arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.BANGLADESH_GREEN)

start_x = 0
start_y = 150
end_x = 600
end_y = 150
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.GHOST_WHITE, 7)

start_x = 0
start_y = 200
end_x = 600
end_y = 200
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.GHOST_WHITE, 6)

start_x = 60
start_y = 200
end_x = 60
end_y = 0
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.GHOST_WHITE, 7)

center_x = 500
center_y = 500
width = 50
height = 80
arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.GHOST_WHITE)

start_x=490
start_y=490
arcade.draw_text('4', start_x, start_y, arcade.color.BLACK, bold=True, font_size=35)

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

start_x = 299
end_x = 301
start_y = 410
end_y = 395
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 1)

start_x = 299
end_x = 301
start_y = 360
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
arcade.draw_text('(', 220, 450, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text(')', 318, 450, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('v', 180, 470, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('v', 328, 470, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('>', 200, 378, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('<', 300, 378, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('<', 300, 513, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('>', 200, 513, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('^', 317, 380, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')
arcade.draw_text('^', 183, 380, arcade.color.BALL_BLUE, 150, 19, 'left', 'calibri')

center_x = 300
center_y = 500
width = 100
height = 120
start_angle = 340
end_angle = 435
arcade.draw_arc_outline(center_x, center_y, width, height, arcade.color.BLACK, start_angle, end_angle, 3)

# Draw shuttle
center_x = 400
center_y = 500
width = 10
height = 10
start_angle = 270
end_angle = 450
arcade.draw_arc_filled(center_x, center_y, width, height, arcade.color.WHITE, start_angle, end_angle)

start_x = 400
start_y = 497
end_x = 380
end_y = 490
while start_y < 505:
    arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.WHITE, 2)
    start_y += 2
    end_y += 6

start_x = 400
start_y = 505
end_x = 400
end_y = 495
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 3)

start_x = 385
start_y = 510
end_x = 385
end_y = 489
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.GHOST_WHITE, 7)

# Draw person
start_x = 200
start_y = 300
end_x = 270
end_y = 400
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BATTLESHIP_GREY, 10)

start_x = 270
start_y = 400
end_x = 260
end_y = 430
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BATTLESHIP_GREY, 10)

center_x = 200
center_y = 400
width = 90
height = 100
arcade.draw_ellipse_filled(center_x, center_y, width, height, arcade.color.ASH_GREY)

start_x = 230
start_y = 420
end_x = 230
end_y = 390
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 10)

start_x = 240
start_y = 370
end_x = 200
end_y = 380
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BLACK, 7)

start_x = 200
start_y = 200
end_x = 120
end_y = 10
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.BATTLESHIP_GREY, 20)

center_x = 200
center_y = 270
width = 40
height = 150
arcade.draw_rectangle_filled(center_x, center_y, width, height, arcade.color.ASH_GREY)

start_x = 200
start_y = 330
end_x = 300
end_y = 290
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.ASH_GREY, 10)

start_x = 250
start_y = 120
end_x = 250
end_y = 10
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.ASH_GREY, 20)

start_x = 200
start_y = 200
end_x = 250
end_y = 120
arcade.draw_line(start_x, start_y, end_x, end_y, arcade.color.ASH_GREY, 20)

# Finish drawing and display the result
arcade.finish_render()

# Keep the window open until the user hits the 'close' button
arcade.run()