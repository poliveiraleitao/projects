######## Challenge 2 - Draw a Dashed Line ############
import turtle as t

timmy_the_turtle = t.Turtle()

for _ in range(50):
    timmy_the_turtle.forward(10) # Length of each dash
    timmy_the_turtle.penup() #stop writing
    timmy_the_turtle.forward(10)  # Gap between dashes
    timmy_the_turtle.pendown() #start writing again

# Keep the window open
t.done()
