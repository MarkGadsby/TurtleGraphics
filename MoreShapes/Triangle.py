from turtle import Turtle, Screen

elsa = Turtle()
window = Screen()

window.bgcolor("brown")

elsa.pencolor("white")
elsa.fillcolor("Yellow")

elsa.begin_fill()

elsa.pensize(10)

for i in range(3):
    elsa.forward(250)
    elsa.left(120)

elsa.end_fill()
 
