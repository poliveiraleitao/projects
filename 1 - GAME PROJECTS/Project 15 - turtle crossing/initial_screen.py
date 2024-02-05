from turtle import Turtle
import time

class Initialscreen(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.game_title()
        time.sleep(1)
        self.clear()

    def game_title(self):
        self.goto(0, 0)
        self.write("WELCOME TO TURTLE CROSSING", align='center', font=('Courier', 24, 'normal'))