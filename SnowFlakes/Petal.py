from turtle import Turtle, Screen

window = Screen()
window.bgcolor("black")

elsa = Turtle()
elsa.pencolor("White")

for i in range(2):
    elsa.forward(50)
    elsa.right(60)
    elsa.forward(50)
    elsa.right(120)
