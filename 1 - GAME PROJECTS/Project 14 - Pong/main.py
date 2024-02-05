from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from initial_screen import Initialscreen
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')

Initialscreen()
screen.tracer(0) #freezes the animation => you will need a code to refresh the screen each time

#paddle location
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# Set initial difficulty
difficulty = 0.1
# Set the value at which the difficulty increases
increase_difficulty_at = 1 #at each x points the difficulty is increased

#make paddle moove
screen.listen()
#right paddle
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

#left paddle
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(difficulty) #changes the game difficulty
    screen.update() #it will update the screen each time you need it
    ball.move()

    #Detect collision with top and lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce on y axis
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330 :
        # need to bounce on x axis
        ball.bounce_x()

    # Detect if r_paddle misses ball and add point to left player
    if ball.xcor() > 380:
        time.sleep(0.2)
        ball.reset_ball()
        ball.bounce_x()
        #add points
        #r_paddle missles ball => l_point
        scoreboard.l_point()

    # Detect if l_paddle misses ball and add point to right player
    if ball.xcor() < -380:
        time.sleep(0.2)
        ball.reset_ball()
        ball.bounce_x()
        # add points
        # l_paddle missles ball => r_point
        scoreboard.r_point()

    # increasing difficulty with time
        # Increase difficulty based on scores
    max_score = max(scoreboard.l_score, scoreboard.r_score)  # Get the higher score
    for threshold in range(1, 5):  # Iterate through difficulty thresholds
        if max_score > threshold:
            difficulty = 0.1 - 0.01 * threshold  # Calculate difficulty value

screen.exitonclick()