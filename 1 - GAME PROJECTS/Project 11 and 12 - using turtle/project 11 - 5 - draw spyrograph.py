###### Challenge 2 - Draw shapes ############
import turtle as t

timmy_the_turtle = t.Turtle()

# Function to generate a random color
def get_random_color():
    color = (random.random(), random.random(), random.random())  # Generates RGB values between 0 and 1
    return color

# Number of circles to draw
num_circles = 50

for _ in range(num_circles):
    timmy_the_turtle.color(get_random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(360 / num_circles)

# Keep the window open
t.done()