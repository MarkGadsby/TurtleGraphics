from turtle import Turtle, Screen

window = Screen()
window.bgcolor("black")

elsa = Turtle()
elsa.speed("fastest")
elsa.setpos(-150,-150)
elsa.pencolor("White")
elsa.fillcolor("White")
#/window.tracer(0)

def SierpinskiTriangles(turtle, depth, size):

    if depth >= 0:
        turtle.begin_fill()

        SierpinskiTriangles(turtle, depth - 1, size / 2)
        turtle.forward(size / 2)

        SierpinskiTriangles(turtle, depth - 1, size / 2)
        turtle.forward(size / 2)
        turtle.left(120)
        turtle.forward(size / 2)

        SierpinskiTriangles(turtle, depth - 1, size / 2)
        turtle.forward(size / 2)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)

        turtle.end_fill()
        
SierpinskiTriangles(elsa,3,500)

#window.update()
        