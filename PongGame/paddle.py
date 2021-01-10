from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_x: int, start_y: int):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x=start_x, y=start_y)

    def go_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def go_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
