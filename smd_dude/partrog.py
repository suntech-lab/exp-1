import arcade

def stickman():
    # Set up the drawing window
    arcade.open_window(400, 400, "Stickman with Smiley Face")
    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()

    arcade.draw_circle_filled(200, 200, 30, arcade.color.BLACK)  # Head
    arcade.draw_line(200, 170, 200, 100, arcade.color.BLACK, 3)  # Body
    arcade.draw_line(200, 150, 230, 130, arcade.color.BLACK, 3)  # Right arm
    arcade.draw_line(200, 150, 170, 130, arcade.color.BLACK, 3)  # Left arm
    arcade.draw_line(200, 100, 230, 70, arcade.color.BLACK, 3)   # Right leg
    arcade.draw_line(200, 100, 170, 70, arcade.color.BLACK, 3)   # Left leg

    arcade.draw_circle_filled(200, 215, 10, arcade.color.YELLOW)  # Draw the face
    arcade.draw_arc_filled(200, 215, 20, 15, arcade.color.BLACK, 180, 360)  # Draw the smile
    arcade.draw_circle_filled(190, 220, 2, arcade.color.BLACK)
    arcade.draw_circle_filled(210, 220, 2, arcade.color.BLACK) 
    arcade.finish_render()

    arcade.run()


stickman()