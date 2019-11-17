from turtle import Turtle, Screen
from random import randint, choice

elsa = Turtle()
elsa.speed("fastest")

colors=['lavender', 'pink', 'blue', 'midnight blue', 'lime']

elsa.pencolor("white")
elsa.pensize(2)

window = Screen()
window.bgcolor("green")

size = 1

elsa.fillcolor("brown")
 
def flower(x,y,r,g,b):
    elsa.setposition(x,y)
    elsa.pendown()
    elsa.color('green')
    elsa.setheading(270)
    elsa.fd(200)
    elsa.setposition(x,y)
    elsa.color(choice(colors))

for i in range(12):
    elsa.circle(20)
    elsa.left(30)
 
 
for i in range(100):
    elsa.penup()
    flower(randint(-200,200), randint(-200,0),randint(0,255), randint(0,255),randint(0,255))    