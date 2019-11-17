from turtle import Turtle, Screen

elsa = Turtle()
screen = Screen()

screen.colormode(255)
elsa.pencolor(255,0,255)
elsa.pensize(2)
elsa.speed(10)

radius = 100

while radius > 10:
    elsa.circle(radius)
    radius -= 20
