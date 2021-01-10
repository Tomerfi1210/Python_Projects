from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__(shape='circle')
        self.penup()
        self.color('red')
        self.__x_move = 10
        self.__y_move = 10
        self.__move_speed = 0.1

    def get_move_speed(self):
        return self.__move_speed

    def move(self):
        self.goto(x=self.xcor() + self.__x_move, y=self.ycor() + self.__y_move)

    def collision_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def bounce_y(self):
        self.__y_move *= -1

    def bounce_x(self):
        self.__x_move *= -1
        self.__move_speed *= 0.9

    def reset_point(self):
        self.goto(0, 0)
        self.__move_speed = 0.1
        self.bounce_x()
