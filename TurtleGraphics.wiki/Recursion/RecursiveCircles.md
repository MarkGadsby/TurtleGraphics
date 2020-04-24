[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  
[Colour Swatch](https://social.technet.microsoft.com/wiki/contents/articles/23237.small-basic-getting-started-guide-appendix-b-colors.aspx)

# Turtle Graphics with Python

## Recursive circles

**Challenge:** Using the circle method can you write some code to draw a circle with a 100 pixel radius?

**Observation:** Note where the drawing starts and stops and in which direction the Turtle is pointing when it’s first initialised.

**Enhancement:** Can you find the methods needed to make the circle draw in a particular colour, line width and speed?

[Circle](https://github.com/MarkGadsby/TurtleGraphics/blob/master/RecursiveCircles/Circle.py)  

---

**Challenge:** Draw concentric circles, that’s circles decreasing in size inside each other. Think about using a while loop with the value for the radius as the controlling variable.

**Observation:** Are the circles all inside each other but not centred?

**Enhancement:** Can we ‘wrap’ the circle() function so that each circle is drawn from it’s centre? Such a enhanced function could go in separate ‘module’ to be imported wherever we need it. 

[Circles Loop](https://github.com/MarkGadsby/TurtleGraphics/blob/master/RecursiveCircles/CirclesFromLoop.py)  

---

> Hints: You can use  xcor() and ycor() to find the current coordinates of the turtle. penup() and pendown() allow you to move the turtle without drawing on the screen  

---

[Using a toolbox](https://github.com/MarkGadsby/TurtleGraphics/blob/master/RecursiveCircles/DrawingToolbox.py)  
[Concentric Circles](https://github.com/MarkGadsby/TurtleGraphics/blob/master/RecursiveCircles/ConcentricCircles.py) 

[Recursing in X](https://github.com/MarkGadsby/TurtleGraphics/blob/master/RecursiveCircles/RecursiveCirclesIn_X.py)  
[Recursing in X and Y](https://github.com/MarkGadsby/TurtleGraphics/blob/master/RecursiveCircles/RecursiveCirclesIn_X_Y.py)  

![DecreasingCrosses](./Recursion/RecursiveCircles.png)

[Home](https://github.com/MarkGadsby/TurtleGraphics/wiki)

