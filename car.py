import random
from turtle import Turtle

COLOR = ["red", "turquoise", "pink", "blue", "green"]
STARTING_SPEED = 1

class Carmanager:
    def __init__(self):
        self.all_cars = []  # List to hold all car objects
        self.car_speed = STARTING_SPEED

    def create_car(self):
        # Only create a car sometimes to avoid too many cars
        random_chance = random.randint(1, 18)
        if random_chance == 1:  # Only add a car 1/3 of the time
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)  # Stretch to make it look like a car
            new_car.penup()
            new_car.color(random.choice(COLOR))
            random_y = random.randint(-260, 260)
            new_car.goto(300, random_y)  # Position the car off-screen to the right
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            # Remove cars that have moved off-screen
            if car.xcor() < -320:  # Assuming screen width is 600
                car.hideturtle()
                self.all_cars.remove(car)

    def level_up(self):
        self.car_speed += 5  # Increase car speed after each level
