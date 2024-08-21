from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.player = Turtle("turtle")
        self.player.penup()
        self.origin()

    def move(self):
        self.player.forward(MOVE_DISTANCE)

    def is_finish_line(self):
        if self.player.ycor() == FINISH_LINE_Y:
            return True

    def origin(self):
        self.player.goto(STARTING_POSITION)
        self.player.setheading(90)
