from turtle import Turtle

FINISH_LINE_Y = 280
STARTING_POSITION = (0, -280)
DEFAULT_SPEED = 1
MOVING_DISTANCE = 15

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)  # Face upwards
        self.speed(DEFAULT_SPEED)

    def move_up(self):
        self.forward(MOVING_DISTANCE)

    def move_back(self):
        self.backward(MOVING_DISTANCE)

    def move_left(self):
        self.left(90)
        self.forward(MOVING_DISTANCE)
        self.right(90)

    def move_right(self):
        self.right(90)
        self.forward(MOVING_DISTANCE)
        self.left(90)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def increase_speed(self, increment):
        self.speed += increment  # You can define how you want to handle speed
