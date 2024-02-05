from turtle import Turtle
import time
import datetime

#highest_score file
FILENAME = 'highest_score.txt'

#font definitions
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

#SCORE POSITION
INITIAL_POSITION = (0, 290)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.read_highest_score() #uses the function read.highest score to return the value
        self.color('white')
        self.penup()
        self.goto(INITIAL_POSITION)  # put the score on top
        self.hideturtle()  # don't show the pointer
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(INITIAL_POSITION)  # put the score on top
        self.clear()  # Clear previous text (or overwrite as needed)
        self.color('white') #game over changs color to red, so we need to change it again
        self.write(f"Score: {self.score} High Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        #update the highest score
        if self.score > self.highest_score:
            self.highest_score = self.score
            self.write_highest_score() #uses function write_highest_score to write it on the file

        self.score = 0
        self.update_scoreboard()

    def show_game_over_screen(self):
        self.goto(0, 0)  # put the GAME OVER sign in the middle of the screen
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.screen.update()  # Force an immediate screen update
        time.sleep(1) #show the gameover sign for 1 second before updating the scoreboard
        self.update_scoreboard()

    def write_highest_score(self):
        with open(FILENAME, mode="a") as file:
            current_datetime = datetime.datetime.now()
            date_time_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{date_time_str} Highest Score: {self.highest_score}\n")

    def read_highest_score(self):
        try:
            with open(FILENAME, mode="r") as file:
                lines = file.readlines()
                for line in reversed(lines):
                    if 'Highest Score:' in line:
                        highest_score = int(line.split(":")[-1].strip())
                        return highest_score
        except FileNotFoundError:
            pass  # File doesn't exist or couldn't be read
        return 0  # Default highest score if no file or no valid content



