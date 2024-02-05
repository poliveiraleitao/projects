from turtle import Turtle, Screen
import random

#define is the rece is happening
is_race_on = False

screen = Screen()
screen.setup(width = 500, height = 400) #always make your code explicit! the 'width' name is optional, but it is good to declare
user_bet = screen.textinput(title = 'Make your Bet', prompt = 'Who will win the race? Enter a color: ')
colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
all_turtles = [] #create a list of turtles

#Start Game

#position turtles
turtle_number = 1

for c in colors:
    new_turtle = Turtle(shape='turtle') #TURTLE SIZE IS 40X40, so to put it in the beggining you must subtract 20 (half the turtle_
    new_turtle.color(c)
    new_turtle.penup()
    new_turtle.goto(x=-230, y =99 - (33 * (turtle_number - 1)))
    turtle_number += 1
    all_turtles.append(new_turtle) #add turtle to list

#start race
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #check end of game
        if turtle.xcor() > 230: #check if turtle reached end of race
            is_race_on = False #end the race

            winning_color = turtle.pencolor() #return the pen color of the turtle
            print('The', winning_color, 'Turtle Won!!')

            #check winner
            if winning_color == user_bet:
                print('Congratulations, you won the bet!!!')
            else:
                print('You Loose the bet!!!')


        #make turtle walk a random distance
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()

