import turtle
import math

screen = turtle.Screen()
screen.addshape(900, 800)


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

    # TODO: romanbrenner, ArtemArkhipov1234, MaximPlotnikovinfa
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

    # TODO: romanbrenner, ArtemArkhipov1234, MaximPlotnikovinfa
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


def Parallel(x, y, size, angle):
    turtle.reset()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    turtle.left(20)

    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

    turtle.left(30)

    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

    turtle.left(40)

    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

    turtle.left(50)

    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

    turtle.left(60)

    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

    turtle.left(70)

    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

    turtle.left(80)

    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)

Parallel(-300, 200, 50, 90)


def Helicopter(x, y):

    turtle.speed(10)

    turtle.reset()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(8)
    turtle.left(90)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(2)
    turtle.left(90)
    turtle.forward(4)
    turtle.left(90)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(4)
    turtle.left(90)
    turtle.forward(8)
    turtle.end_fill()

    turtle.right(90)
    turtle.penup()
    turtle.forward(88)
    turtle.pendown()
    turtle.right(90)

    turtle.begin_fill()
    turtle.forward(8)
    turtle.right(90)
    turtle.forward(4)
    turtle.left(90)
    turtle.forward(2)
    turtle.right(90)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(2)
    turtle.left(90)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(8)
    turtle.end_fill()

    turtle.left(90)
    turtle.penup()
    turtle.forward(38)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)

    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)

    turtle.right(90)
    turtle.forward(50)
    turtle.left(135)

    turtle.begin_fill()
    turtle.circle(35, 90)
    turtle.end_fill()

    turtle.penup()
    turtle.left(135)
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()

    turtle.forward(150)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(30)
    turtle.right(150)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(30)
    turtle.left(60)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(100)
    turtle.pendown()

    turtle.left(30)
    turtle.forward(58)

    turtle.penup()
    turtle.right(31)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(2)
    turtle.pendown()

    turtle.forward(20)
    turtle.right(70)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(150)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(50)

Helicopter(-500, -300)


from turtle import Turtle, Screen

def Flower(turtle, radius):
    heading = turtle.heading()
    turtle.circle(radius, 60)
    turtle.left(120)
    turtle.circle(radius, 60)
    turtle.setheading(heading)

my_radius = int(100)
my_petals = int(10)

turtle = Turtle()

for _ in range(10):
    Flower(turtle, 100)
    turtle.left(360 / 10)

turtle.hideturtle()

screen = Screen()
screen.exitonclick()





