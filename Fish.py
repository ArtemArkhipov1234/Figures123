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

    # TODO: romanbrenner, ArtemArkhipov1234
    pass


def triangle(x, y, size, color, angle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.right(angle)
    turtle.right(30)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(30)
    turtle.end_fill()

    # TODO: romanbrenner, ArtemArkhipov1234
    pass



turtle.speed(5)

def fish(x, y, size, color, angle):
    square(x, y, 100, "yellow", 0)
    triangle(x + 100, y, 100, "green", 90)
    triangle(x, y - 100, 75, "red", 150)
    triangle(x, y, 75, "red", 120)
    square(x - 0, y, 100, "yellow", 0)
    turtle.penup()
    turtle.goto(-190, -300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.end_fill()


fish(-10, -200, "red",0 , 0)

turtle.mainloop()




