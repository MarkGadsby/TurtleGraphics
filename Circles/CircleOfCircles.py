from math import cos, sin
from turtle import Turtle, Screen

elsa = Turtle()
window = Screen()

window.colormode(255)


window.bgcolor(250,25,250)

elsa.speed("fastest")
elsa.pensize(2)


def DrawCircle(x,y):
    elsa.setpos(x, y)
    elsa.circle(200)

for i in range(0, 640, 17):
    x = 0.00
    y = 0.00
    x = sin(i/100) * 100
    y = cos(i/100) * 100
    DrawCircle(x, y)
 
