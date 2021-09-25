from turtle import Screen
import time

from snake_game.food import Food
from snake_game.scoreboard import Score
from snake_game.snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("snow2")
screen.title(">>SANKE<<")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
