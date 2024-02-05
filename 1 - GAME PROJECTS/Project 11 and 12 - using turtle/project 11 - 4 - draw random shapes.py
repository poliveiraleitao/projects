###### Challenge 2 - Draw shapes ############
import turtle as t
import random

timmy_the_turtle = t.Turtle()

# Function to generate a random color
def get_random_color():
    color = (random.random(), random.random(), random.random())  # Generates RGB values between 0 and 1
    return color

for x in range(4, 15):
    timmy_the_turtle.color(get_random_color())
    for _ in range (x):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(360 / x)
    x +=1

# Keep the window open
t.done()