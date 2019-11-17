from turtle import Turtle, Screen

elsa = Turtle()
elsa.speed("fastest")

elsa.pencolor("white")
elsa.pensize(2)

window = Screen()
window.bgcolor("green")

window.tracer(0)

def star(turtle, n, r):
    for k in range(n):
        turtle.pendown()
        turtle.forward(r)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360/n)
 
def recursive_star(turtle, n, r, depth, f):
    if depth == 0:
        star(turtle, n, f * 4)
    else:
        for k in range(n):
            turtle.pendown()
            turtle.forward(r)
            recursive_star(turtle, n, f * r, depth - 1, f)
            turtle.penup()
            turtle.backward(r)
            turtle.left(360/n)
 
recursive_star(elsa ,5 ,200, 4, 0.4)

window.update()