from turtle import Turtle, Screen

elsa = Turtle()
window = Screen()

window.colormode(255)
window.bgcolor(0,0,0)

elsa.speed("fastest")
elsa.pensize(2)
elsa.pencolor(255,255,255)

#window.tracer(0)

for count in range(0, 10):
#    elsa.forward(count // 3) 
#    elsa.pencolor(count * 20 % 255, count  * 10 % 255, count * 50 % 255)
#    elsa.fillcolor(count * 5 % 255, count  * 10 % 255, count * 20 % 255)
#    elsa.begin_fill()
    elsa.right(36)
    elsa.circle(100)
#    elsa.end_fill()

#window.update()  
