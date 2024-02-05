from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 225)
        self.write(f"{self.l_score}", align='center', font=('Courier', 50, 'normal'))
        self.goto(0, 225)
        self.write('|', align='center', font=('Courier', 50, 'normal'))
        self.goto(150, 225)
        self.write(f"{self.r_score}", align='center', font=('Courier', 50, 'normal'))
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()


