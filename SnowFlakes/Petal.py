from turtle import Turtle, Screen
from random import randint

window = Screen()
window.bgcolor("black")

elsa = Turtle()
elsa.pencolor("White")
elsa.fillcolor("White")

for i in range(2):
    elsa.forward(50)
    elsa.right(60)
    elsa.forward(50)
    elsa.right(120)