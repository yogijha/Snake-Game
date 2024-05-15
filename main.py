from turtle import Turtle, Screen
import time
from snake import Snack
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snack()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
food = Food()
scoreboard = Scoreboard()
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_segment()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
