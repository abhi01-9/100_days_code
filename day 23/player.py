from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 5


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.go_to_start()
        self.move_steps = MOVE_DISTANCE

    def go_up(self):
        self.forward(self.move_steps)

    def move_bottom(self):
        self.goto(STARTING_POSITION)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def increase_move_speed(self):
        self.move_steps += MOVE_INCREMENT
