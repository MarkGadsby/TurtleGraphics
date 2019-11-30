from turtle import Turtle, Screen

window = Screen()
window.bgcolor("black")
window.setup(800,800)

elsa = Turtle()
elsa.speed("fastest")
elsa.pencolor("White")
elsa.penup()

def splay():
    elsa.pendown()
    elsa.left(45)
    elsa.forward(40)
    elsa.backward(40)
    elsa.right(90)
    elsa.forward(40)
    elsa.backward(40)
    elsa.left(45)
    elsa.forward(40)
    elsa.backward(40)
    elsa.penup()
    
splay()
elsa.forward(35)
splay()
elsa.forward(35)
splay()
elsa.backward(70)