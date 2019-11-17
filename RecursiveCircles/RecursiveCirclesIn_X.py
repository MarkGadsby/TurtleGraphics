from turtle import Turtle, Screen
from DrawingToolbox import DrawCentredCircle

elsa = Turtle()
screen = Screen()

screen.colormode(255)
screen.bgcolor(0,0,0)
elsa.pencolor(255,255,255)
elsa.pensize(2)
elsa.speed("fastest")

def DrawCirclePattern(turtle,  x, y, radius):
    turtle.setpos(x, y)
    DrawCentredCircle(turtle, radius)
    if radius > 20:
        DrawCirclePattern(turtle, x - radius, y, radius/2)
        DrawCirclePattern(turtle, x + radius, y, radius/2)
 
DrawCirclePattern(elsa, 0, 0, 200)


