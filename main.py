from turtle import Screen
import time
from Snake import Snake
from food import Food
from score import Score

screen = Screen()

screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake game')

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.print_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False
        


screen.exitonclick()
