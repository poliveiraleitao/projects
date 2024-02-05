from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 285
INITIAL_LINE_Y = -285

class Player(Turtle):
    # beggins the game creating 1 turtle on the bottom of the screen
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.left(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

#make turtle move
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < FINISH_LINE_Y:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > INITIAL_LINE_Y:
            self.goto(self.xcor(), new_y)

    def is_at_finish_line(self):
        if self.ycor() > (FINISH_LINE_Y - 10):
            return True

    def go_to_start(self):
        self.goto(STARTING_POSITION)
