import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from initial_screen import Initialscreen

#setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')

Initialscreen()
screen.tracer(0)

# Create the player outside the game loop
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#defining movements
screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_down, 'Down')

# Initialize the game state
game_is_on = True

while game_is_on:
    screen.update() #print the frame on the screen ( see screen.tracer)
    time.sleep(0.1) #the smaller the number the faster the game will be!!
    car_manager.create_car()
    car_manager.move_cars()

    #check for collision
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            print("Game Over")
            game_is_on = False
            scoreboard.game_over()

    # check if player won
    if player.is_at_finish_line():
        print("Congratulations!! You Won!")
        car_manager.level_up()
        scoreboard.increase_level()
        time.sleep(2)
        player.go_to_start()

screen.exitonclick()
