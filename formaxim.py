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
    triangle(x - 50, y, 50, "red", 90)
    triangle(x, y - 50, 50, "red", 90)
    triangle(x, y + 50, 50, "red", 90)
rhombus(500, 400, 100, "red", 0)


def house(x, y, size, color, angle):
    square(x, y, 100, "green", 0)
    triangle(x, y, 100, "red", 0)
    turtle.penup()
    turtle.right(180)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    square(x + 60, y - 40, 30, "black", 0)
    square(x + 44, y - 50, 10, "yellow", 0)


house(100, 200, 100, "red", 0)



