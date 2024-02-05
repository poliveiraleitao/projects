from turtle import Turtle

STARTING_POSITIONS = [(-350,0), (350, 0)]
MOVE_DISTANCE = 20

class Paddle(Turtle):
    #beggins the game creating 2 paddles on each side of the screen
    def __init__(self, position):
        super().__init__() #to enherity all the atributes of the turtle class as well
        self.shape('square')
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

#make paddle move
    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)