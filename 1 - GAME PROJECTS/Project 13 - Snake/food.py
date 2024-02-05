from turtle import Turtle

import random

class Food(Turtle): #(Turtle) will give the class food all the atribuites of the turtle class
    def __init__(self):
        super().__init__() #this is just a method to give the atributes of the turtle class
        #the properties bellow are from the Turtle class
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5) #divide len and wid by 2
        self.color('green')
        self.speed('fastest') #define the speed that the food changes place
        random_x = random.randint(-280, 280) #the canvas is 600 x 670, but we are leaving a margin of 20
        random_y = random.randint(-315, 280) #so that the food is not created right on the edge of the screen
        self.goto(random_x, random_y)

    def refresh_food(self):
        random_x = random.randint(-280, 280)  # the canvas is 600 x 600, but we are leaving a margin of 20
        random_y = random.randint(-315, 280)  # so that the food is not created right on the edge of the screen
        self.goto(random_x, random_y)