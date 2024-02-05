from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)
def spin_right():
    tim.right(18)
def spin_left():
    tim.left(18)

screen.listen()
screen.onkey(key='space', fun = move_forward)
screen.onkey(key='Left', fun = spin_left)
screen.onkey(key='Right', fun = spin_right)
screen.exitonclick()