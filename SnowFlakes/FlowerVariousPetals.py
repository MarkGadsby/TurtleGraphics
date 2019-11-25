from turtle import Turtle, Screen

window = Screen()
window.bgcolor("black")

elsa = Turtle()
elsa.speed("fastest")
elsa.pencolor("White")
elsa.fillcolor("White")
elsa.penup()

def DrawFlower(nPetals):
    elsa.pendown()
    for Petal in range(nPetals):
        for i in range(2):
            elsa.forward(50)
            elsa.right(60)
            elsa.forward(50)
            elsa.right(120)
        elsa.right(360/nPetals)
    elsa.penup()
        
elsa.setpos(0,0)
DrawFlower(5)
elsa.setpos(-150,-150)
DrawFlower(7)
elsa.setpos(150,-150)
DrawFlower(12)
elsa.setpos(-150,150)
DrawFlower(20)
elsa.setpos(150,150)
DrawFlower(16)   
