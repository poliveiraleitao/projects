from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20 # it is set at 20 so that the white blocks walk a full new block ahead
#defining the angle of movement
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    #beggins the game creating 3 segments and starting the movement
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #create to manipulate the head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #make snake grown as it eats food
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()  # avoid segments from drawing a line as they move
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

           # make snake move
           # to move properly, the last segment most fo to the position of the n-1 segment and so on..
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # start with third segment and go to first
            new_x = self.segments[seg_num - 1].xcor()  # new x cor of the seg = x cor of the next seg
            new_y = self.segments[seg_num - 1].ycor()  # new y cor of the seg = y cor of the next seg
            self.segments[seg_num].goto(new_x, new_y)

       # make first segment walk forward
        self.head.forward(MOVE_DISTANCE)  # it is set at 20 so that the white blocks walk a full new block ahead

    def reset_snake(self):
        time.sleep(0.5)
        #first you need to send all the segment turtles to a place you can´t see
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]  # create to manipulate the head of the snake


    #making the snake turn to the desirable direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
