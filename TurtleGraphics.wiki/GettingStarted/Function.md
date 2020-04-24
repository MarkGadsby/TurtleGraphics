[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  
[Colour Swatch](https://social.technet.microsoft.com/wiki/contents/articles/23237.small-basic-getting-started-guide-appendix-b-colors.aspx)

# Turtle Graphics with Python

## Adding a function

 - If we want to be able draw a number of crosses in different positions on the screen. It means repeating the cross drawing code, but there is a much better way to this
 - We can create a **function** called DrawCross() like this

![DrawCross](./GettingStarted/DrawCross.png)  

> TIP - the DrawCross() function has to defined in your code 'before' you can call it. So place DrawCross() near the top of your file.   

1. Add `DrawCross()` to your code and call it draw a cross in the middle of the screen

2. Can you use this pattern:

  `elsa.penup()`  
  `elsa.setpos(150,150)`  
  `elsa.pendown()`  
  `DrawCross()`  

  to draw crosses in each of the four quadrants in the screen?

![Crosses](./GettingStarted/Crosses.png)  

[Home](https://github.com/MarkGadsby/TurtleGraphics/wiki)
