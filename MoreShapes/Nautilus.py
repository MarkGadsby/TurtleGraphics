#"A nautilus shape"

from turtle import Turtle, Screen

elsa = Turtle()
elsa.speed("fastest")

elsa.pencolor("black")
elsa.pensize(1)

window = Screen()

window.bgcolor("brown")

size = 1

elsa.fillcolor("rosybrown")

for i in range(36*3):
    elsa.begin_fill()
    for i in range(4):
          elsa.forward(size)
          elsa.right(90)
          size += 1
    elsa.right(5)
    elsa.end_fill()
