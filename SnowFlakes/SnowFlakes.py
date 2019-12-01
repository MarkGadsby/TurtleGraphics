from turtle import Turtle, Screen
from random import randint

window = Screen()
window.bgcolor("black")
window.setup(800,800)

elsa = Turtle()
elsa.speed("fastest")
elsa.pencolor("White")
elsa.fillcolor("White")
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
    
def branch():
    splay()
    elsa.forward(35)
    splay()
    elsa.forward(35)
    splay()
    elsa.backward(70)

def DrawSnowflake():
    numberOfBranches = randint(4,30)
    for i in range(numberOfBranches):
        branch()
        elsa.left(360/numberOfBranches)    

elsa.setpos(150,150)
DrawSnowflake()
elsa.setpos(-100,-100)
DrawSnowflake()



