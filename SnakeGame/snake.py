from turtle import Turtle, Screen

STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.__m_segments = []
        self.__create_snake()
        self.__head = self.__m_segments[0]

    def __create_snake(self):
        for position in STARTING_POSITION:
            self.__add_segment(position)

    def __add_segment(self, position):
        self.__m_segments.append(Turtle(shape='square'))
        self.__m_segments[-1].color('white')
        self.__m_segments[-1].penup()
        self.__m_segments[-1].goto(position)

    def extend(self):
        self.__add_segment(self.__m_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.__m_segments) - 1, 0, -1):
            self.__m_segments[seg_num].goto(self.__m_segments[seg_num - 1].xcor(),
                                            self.__m_segments[seg_num - 1].ycor())
        self.__head.forward(MOVE_DISTANCE)

    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)

    def get_head(self):
        return self.__head

    def collison_with_tail(self):
        for segment in self.__m_segments[1:]:
            if self.__head.distance(segment) < 10:
                return True
        return False
