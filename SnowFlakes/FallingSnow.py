from turtle import Turtle, Screen
from random import randint
from random import random

window = Screen()
window.bgcolor("black")
window.setup(800,800)
window.tracer(0)

# turtle details list
Turtles = [Turtle(), 6, 0, 400, Turtle(), 6, -400, 400, Turtle(), 6, -200, 500, Turtle(), 6, 200, 400, Turtle(), 6, 400, 500] 

def splay(turt):
    turt.pendown()
    turt.left(45)
    turt.forward(40)
    turt.backward(40)
    turt.right(90)
    turt.forward(40)
    turt.backward(40)
    turt.left(45)
    turt.forward(40)
    turt.backward(40)
    turt.penup()
    
def branch(turt):
    splay(turt)
    turt.forward(35)
    splay(turt)
    turt.forward(35)
    splay(turt)
    turt.backward(70)

def DrawSnowflake(turt, branches):
    for i in range(branches):
        branch(turt)
        turt.left(360/branches)
        
def FallingSnowFlake(turt, branches, xPos, yPos):
    turt.pencolor("white")
    turt.setpos(xPos,yPos)
    DrawSnowflake(turt,branches)
    turt.hideturtle()


def frame ():
    global Turtles
    
    for i in range (5):
        if (Turtles[(i * 4) + 3] < -400):
            Turtles[(i * 4) + 1] = randint(6,18)
            Turtles[(i * 4) + 2] = randint(-400,400)
            Turtles[(i * 4) + 3] = 400

    for i in range (5):
        Turtles[(i * 4) + 0].clear()

    Turtles[3] -= 1
    Turtles[7] -= 2
    Turtles[11] -= 3
    Turtles[15] -= 1.5
    Turtles[19] -= 2.5

    for i in range(5):
        FallingSnowFlake(Turtles[(i * 4) + 0], Turtles[(i * 4) + 1], Turtles[(i * 4) + 2], Turtles[(i * 4) + 3])               
   
    window.update()                      # show the new frame
    window.ontimer(frame, framerate_ms)  # schedule this function to be called again a bit later

framerate_ms = 1 # Every how many milliseconds must frame function be called?
frame()

    
    
