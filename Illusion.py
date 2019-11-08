import turtle


bgcolor("gray")

pu()
speed(0)
ht()
shape("square")
shapesize(3.2, 3.5)

shift = [10, 0, 10, 28, 10, 0, 10, 28, 10]

tracer(False)
for i in range(9):
    goto(-365 + shift[i], 267-66*i)
    color("black")
    for i in range(11):
        stamp()
        fd(70)
        if pencolor() == "white":
            color("black")
        else:
            color("white")
mainloop()
