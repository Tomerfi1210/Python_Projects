from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

if __name__ == '__main__':
    screen = Screen()
    screen.bgcolor('black')
    screen.setup(width=800, height=600)
    screen.title(' ' * 110 + 'Pong')
    screen.tracer(0)

    r_paddle = Paddle(350, 0)
    l_paddle = Paddle(-350, 0)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')

    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')

    is_game_on = True
    while is_game_on:
        time.sleep(ball.get_move_speed())
        screen.update()
        ball.move()

        # Detect collision with the wall
        if ball.collision_wall():
            ball.bounce_y()

        # Detect collision with r_paddle
        elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
                ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()

        elif ball.xcor() > 380:
            ball.reset_point()
            scoreboard.l_point()

        elif ball.xcor() < -380:
            ball.reset_point()
            scoreboard.r_point()

    screen.exitonclick()
