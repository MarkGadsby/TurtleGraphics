# "A spiral out of squares"
from turtle import Turtle, Screen

elsa = Turtle()
window = Screen()

window.bgcolor("black")
elsa.speed("fastest")
elsa.pencolor("white")

elsa.pensize(2)

size = 1

for i in range(250):
    if i % 2:
        elsa.pencolor("white")
    else:
        elsa.pencolor("rosybrown")
    elsa.forward(size)
    elsa.right(92)
    size = size + 2