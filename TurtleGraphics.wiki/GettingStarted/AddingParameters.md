[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  
[Colour Swatch](https://social.technet.microsoft.com/wiki/contents/articles/23237.small-basic-getting-started-guide-appendix-b-colors.aspx)

# Turtle Graphics with Python

## Adding parameters to a function

![DecreasingCrosses](./GettingStarted/DecreasingCrosses.png)  

See the code file:

[TurtleCrosses.py](https://github.com/MarkGadsby/TurtleGraphics/blob/master/Crosses/TurtleCrosses.py)

I have added two functions; `DrawCross(size)` and `PositionCrosses(halfScreenWidth, pensize)`

`PositionCrosses` calls `DrawCross` to put a cross in each of the four quadrants of the screen, **but also** keeps calling 'DrawCross` each time halving the distance from the cross to the middle of the screen and halving the pensize to use. The crosses size is calculated to be 1/3 of the distance to the middle.

[Home](https://github.com/MarkGadsby/TurtleGraphics/wiki)
