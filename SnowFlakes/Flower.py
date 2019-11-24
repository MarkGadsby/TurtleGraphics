from turtle import Turtle, Screen

window = Screen()
window.bgcolor("black")

elsa = Turtle()
elsa.speed("fastest")
elsa.pencolor("White")
elsa.fillcolor("White")
elsa.penup()

def DrawFlower():
    elsa.pendown()
    for Petal in range(10):
        for i in range(2):
            elsa.forward(50)
            elsa.right(60)
            elsa.forward(50)
            elsa.right(120)
        elsa.right(36)
    elsa.penup()

DrawFlower()