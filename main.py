from turtle import Screen
from snake_body import SnakeBody
from food import Food
import time

# create the game board
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# create game element
snake = SnakeBody()

food = Food()

# set the snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over= False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
     # detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()

screen.exitonclick()
