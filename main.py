from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

game_is_on = True

# Added these to adjust based on any different screen dimension constants used
# and accounts for edge of ball
top_wall = int(SCREEN_HEIGHT / 2) - 20
bottom_wall = -int(SCREEN_HEIGHT / 2) + 23
right_wall = int(SCREEN_WIDTH / 2) - 20
left_wall = -int(SCREEN_WIDTH / 2) + 15

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Draw net
net = Turtle()
top_of_net = int(SCREEN_HEIGHT / 2) - 15
net_length = SCREEN_HEIGHT

screen.tracer(0)
net.goto(0, top_of_net)
net.setheading(270)
net.pencolor("white")
net.pensize(5)
net.hideturtle()
for _ in range (19):
    net.forward(20)
    net.penup()
    net.forward(10)
    net.pendown()
screen.update()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball((0, 0))

scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > top_wall or ball.ycor() < bottom_wall:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        ball.boost_speed()

    # Detect if R Paddle misses:
    if ball.xcor() > right_wall:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if L Paddle misses:
    if ball.xcor() < left_wall:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()


