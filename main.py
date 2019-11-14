import turtle,time

screen = turtle.Screen()

screen.addshape(900, 800)

def star(x, y, n, dlina, color):
    turtle.reset()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.color(color)
    turtle.forward(dlina)
    angle = 80
    turtle.left(angle)

star(-300, -200, 9, 150, 'red')

