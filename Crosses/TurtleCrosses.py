from turtle import Turtle, Screen

def DrawCross(size):
    elsa.pendown()
    elsa.forward(size)
    elsa.backward(size * 2)
    elsa.forward(size)
    elsa.left(90)
    elsa.forward(size)
    elsa.backward(size * 2)
    elsa.forward(size)
    elsa.penup()

def PositionCrosses(halfScreenWidth, pensize):
    while halfScreenWidth > 1:
        elsa.pensize(pensize)
        elsa.setpos(halfScreenWidth,halfScreenWidth)
        DrawCross(halfScreenWidth/3)
        elsa.setpos(-halfScreenWidth,-halfScreenWidth)
        DrawCross(halfScreenWidth/3)
        elsa.setpos(halfScreenWidth,-halfScreenWidth)
        DrawCross(halfScreenWidth/3)
        elsa.setpos(-halfScreenWidth,halfScreenWidth)
        DrawCross(halfScreenWidth/3)
        halfScreenWidth /= 2
        pensize /= 2

elsa = Turtle()
elsa.speed("fastest")

window = Screen()
window.setup(600,600)

elsa.pencolor("white")
window.bgcolor("darkred")
elsa.penup()
PositionCrosses(300,30)
elsa.hideturtle()

