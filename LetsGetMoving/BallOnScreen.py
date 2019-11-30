from turtle import Turtle, Screen

window = Screen()

window.setup(800,600)
window.bgcolor("cornflowerblue")
# Ball
ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("red")
ball.shapesize(1)
