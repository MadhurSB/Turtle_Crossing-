import random
from turtle import Turtle, Screen
from car import Carmanager
from player import Player
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Turtle Crossing")

# Initialize objects
player = Player()
cars = Carmanager()
scoreboard = Scoreboard()

# Keyboard controls
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_back, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    
    cars.create_car()
    cars.move_cars()

    # Check for collision with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if the player reached the finish line
    if player.is_at_finish_line():
        player.reset_position()  # Reset the player's position
        cars.level_up()          # Increase car speed
        scoreboard.increase_Level()

screen.exitonclick()
