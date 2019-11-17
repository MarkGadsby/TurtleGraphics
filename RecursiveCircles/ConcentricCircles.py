from turtle import Turtle, Screen
from DrawingToolbox import DrawCentredCircle
from random import randint

elsa = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor(0,0,0)

elsa.pencolor(255,255,255)
elsa.pensize(2)
elsa.speed(10)

radius = 200

colours = ['lavender', 'pink', 'blue', 'midnight blue', 'lime']

while radius > 10:
    elsa.fillcolor(colours[randint(0,4)])
    elsa.begin_fill()
    DrawCentredCircle(elsa,radius)
    radius -= 30
    elsa.end_fill()
