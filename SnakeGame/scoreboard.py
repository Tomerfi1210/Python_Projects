from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto((0, 260))
        self.hideturtle()
        self.__score = 0
        self.__update()

    def __update(self):
        self.write(f'Score: {self.__score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write('GAME OVER', align=ALIGN, font=FONT)

    def increase(self):
        self.__score += 1
        self.clear()
        self.__update()