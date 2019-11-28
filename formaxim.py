import turtle
def square(x, y, size, color, angle):
    turtle.penup()
    turtle.goto(x, y)  # черепашку на координаты
    turtle.pendown()
    turtle.begin_fill()  # начать заполнять цветом
    turtle.color(color)  # выбор цвета
    turtle.right(angle)  # угол, под которым рисовать квадрат(первый)
    turtle.forward(size)  # первая сторона, её длина
    turtle.right(90)  # второй угол квадрата
    turtle.forward(size)  # вторая сторона, её длина
    turtle.right(90)  # третий угол квадрата
    turtle.forward(size)  # третья сторона, её длина
    turtle.right(90)  # четвёртый угол квадрата
    turtle.forward(size)  # чертвёртая сторона, её длина
    turtle.end_fill()  # закончить заполнение цветом

    # TODO: romanbrenner, ArtemArkhipov1234
    pass


def triangle(x, y, size, color, angle):
    turtle.penup()
    turtle.goto(x, y)  # черепашку на координаты х и у
    turtle.pendown()
    turtle.begin_fill()  # начать заполнять цветом
    turtle.color(color)  # выбор цвета
    turtle.right(angle)  # угол, под которым будет рисоваться треугольник
    turtle.right(30)  # поворот черепашки(1 угол треугольника)
    turtle.forward(size)  # первая сторона треугольника
    turtle.right(120)  # второй угол треугольника
    turtle.forward(size)  # вторая сторона треугольника
    turtle.right(30)  # третий угол треугольника
    turtle.end_fill()  # закончить заполнение цветом + авто-дорисовка треугольника

    # TODO: romanbrenner, ArtemArkhipov1234
    pass

def rhombus(x, y, size, color, angle):
    square(x, y, 50, "blue", 0)
    triangle(x + 50, y, 50, "red", 90)
    triangle(x - 44, y - 25, 50, "red", 120)
    triangle(x + 50, y - 50, 50, "red", 330)
    triangle(x + 24, y + 44, 50, "red", 120)

rhombus(0, 0, 100, "red", 0)


turtle.mainloop()