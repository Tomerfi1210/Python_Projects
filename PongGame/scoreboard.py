from turtle import Turtle

FONT = ('Courier', 60, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.__l_score = 0
        self.__r_score = 0
        self.__update_scoreboard()

    def __update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(self.__l_score, align=ALIGN, font=FONT)
        self.goto(x=100, y=200)
        self.write(self.__r_score, align=ALIGN, font=FONT)

    def l_point(self):
        self.__l_score += 1
        self.__update_scoreboard()

    def r_point(self):
        self.__r_score += 1
        self.__update_scoreboard()
