[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  

# Turtle Graphics with Python

## Understanding screen coordinates

 - The turtle (elsa) will start in the middle of the screen
 - We set the screen to be 600 x 600 pixels
 - The coordinates in the middle are 0,0
 - So the top left hand corner of the screen is 300,300
 - The bottom right is -300, -300

 1. Lets add some code that will draw a cross using forward() and backward() like we have seen before and a new fuction call left().

 `elsa.forward(30)`  
 `elsa.backward(60)`   
 `elsa.forward(30)`  
 `elsa.left(90)` *Turn to face 90 degrees left*  
 `elsa.forward(30)`  
 `elsa.backward(60)`  
 `elsa.forward(30)`  

2. Save and run the code, you should see a cross in the middle of the screen.

  - The function that positions elsa on the screen is called setpos() e.g. `elsa.setpos(0,0)`
  - We don't have call it because elsa 'defaults' to the middle of the screen anyway.  


3. Add `elsa.setpos(150,150)` to your code (before elsa draws the cross) so the cross is drawn in the top left quadrant of the screen. Save and run the code, has the cross moved?

4. Can you send elsa to the bottom right quadrant of the screen to draw the TurtleCrosses?

5. Can use the functions called `elsa.penup()` and `elsa.pendown()` to make sure only the cross is drawn?  

[Next, Adding a function](https://github.com/MarkGadsby/TurtleGraphics/wiki/Function)