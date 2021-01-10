from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title(f" {' ' * 70} Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()


    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.07)
        snake.move()

        #Detect collision with food
        if snake.get_head().distance(food) < 15:
            food.move()
            scoreboard.increase()
            snake.extend()

        #Detect collision with wall
        if snake.get_head().xcor() > 280 or\
                snake.get_head().xcor() < -300 or \
                snake.get_head().ycor() > 300 or \
                snake.get_head().ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail
        if snake.collison_with_tail():
            game_is_on = False
            scoreboard.game_over()

    screen.mainloop()
