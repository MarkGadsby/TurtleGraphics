[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)
# Turtle Graphics with Python

## Getting started

### Getting turtle graphics into your program:

1. Start IDLE
2. Open and save a new file called TurtleCrosses.py  

>    - *TIP - make a new folder called PythonTurtleGraphics in your shared area and save the TurtleCrosses.py in that folder*


3. At the top of the file add the following import statement:  

 `from turtle import Turtle, Screen` *this means import some 'object templates' called Turtle and Screen into your program for you to use*

4. Make the two objects we want to use.

 `elsa = Turtle()`*create an actual Turtle called elsa (or whatever you like)*

 `elsa.shape("turtle")`*give elsa the shape of a turtle*

 `window = Screen()` *.. and an actual Screen called window*

5. Set our window up by calling:

  `window.setup(600,600)` *this sets our window to a size of 600 pixels by 600 pixels*

6. Use elsa to draw a line on the screen:

  `elsa.forward(100)`

7. Save and run the code.

8. Can you edit the code to make elsa draw a longer line?
9. Can you edit the code to make elsa move backwards?  

[Next, Adding colours](https://github.com/MarkGadsby/TurtleGraphics/wiki/AddingColours)

