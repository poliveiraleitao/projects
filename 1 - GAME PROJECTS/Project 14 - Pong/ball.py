from turtle import Turtle

MOVE_DISTANCE = 20

class Ball(Turtle):
    #beggins the game creating 1 ball in the middle of the screen
    def __init__(self):
        super().__init__() #to enherity all the atributes of the turtle class as well
        self.shape('circle')
        self.color("white")
        self.penup()
        self.x_move = 10 #sets how many pixels the ball walks at each frame
        self.y_move = 10 #sets how many pixels the ball walks at each frame

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0, 0)


