from turtle import Turtle, Screen, turtles
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time 


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


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

    #detect collision with food
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.exend()
        scoreboard.refresh()


    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        scoreboard.reset()
        snake.reset()


    
    #Deteck collision with any segment in the tail:
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()












