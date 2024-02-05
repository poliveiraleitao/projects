from turtle import Screen
from turtle import Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from initial_screen import Initialscreen
import time

#defining screen
screen = Screen()
screen.setup(width = 600, height = 670)
screen.bgcolor('black')
screen.title('Snake Game!')
Initialscreen()
screen.tracer(0) #avoid animation of the snake! what we will do istead is to redraw everything at each frame

#drawing line bellow the score
line_turtle = Turtle()  # Create a separate turtle for the line
line_turtle.speed(0)  # Set speed to fastest
line_turtle.color('white')  # Set a visible color
line_turtle.hideturtle()  # Hide the turtle itself
line_turtle.penup()
line_turtle.goto(-300, 280)  # Adjust coordinates as needed
line_turtle.pendown()
line_turtle.forward(600)  # Adjust length as needed

#define snake class for the main game
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#defining movements
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update() #print the frame on the screen ( see screen.tracer)
    time.sleep(0.1) #the smaller the number the faster the game will be!!
    snake.move()

    #detect collision with food!!!!
    if snake.head.distance(food) <= 17: #food is 10x10 so with 15 we can be pretty sure it collided
        food.refresh_food() #changes location of food
        snake.extend_snake()
        scoreboard.increase_score() #increases the score

    #detect collision with wall!!!!
    #remember y goes from -335 to +300, because above that is the white line
    if (
        snake.head.xcor() > 295
        or snake.head.xcor() < -295
        or snake.head.ycor() > 295
        or snake.head.ycor() < -325
    ): #canvas is 600 x 370 so this will make sure the head is almost touching the wall
        scoreboard.show_game_over_screen()
        time.sleep(2)
        scoreboard.reset()
        snake.reset_snake()

    #detect collision with own tail!!!!
    #if head collides with any segment in the tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.show_game_over_screen()
            time.sleep(2)
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
