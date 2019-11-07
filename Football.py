
import turtle, random

window = turtle.Screen()
border = turtle.Turtle
border.speed(0)
border.up()
border.hideturtle()
border.pensize(5)
border.color('red')
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

ball = turtle.Turtle()
ball.shape('circle')
ball.up()
dx = 3
dy = 4
