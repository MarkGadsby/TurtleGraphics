def DrawCentredCircle(turtle, radius):
    turtle.penup()
    turtle.setpos(turtle.xcor(), turtle.ycor() - radius)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.setpos(turtle.xcor(), turtle.ycor() + radius)
