import turtle


def square(x, y, size, color, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.right(angle)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    # TODO: romanbrenner, ArtemArkhipov1234
    pass


def triangle(x, y, size, color, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.right(angle)
    turtle.forward(size)
    turtle.right(angle)
    turtle.forward(size)
    turtle.right(angle)
    turtle.forward(size)
    turtle.right(angle)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    # TODO: romanbrenner, ArtemArkhipov1234
    pass


def circle(size, color)
    turtle.penup()
    turtle.goto()
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(size)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
    # TODO: romanbrenner, ArtemArkhipov1234
