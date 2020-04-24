[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  
[Colour Swatch](https://social.technet.microsoft.com/wiki/contents/articles/23237.small-basic-getting-started-guide-appendix-b-colors.aspx)

# Turtle Graphics with Python

## Recursive triangles

### Sierpinski triangles

This is a image of a Sierpinski triangle broken down by five levels:

![SierpinskiTriangles](./Images/SierpinskiTriangles.png)  

The rules of a Sierpinski triangle are that you draw an outer equilateral triangle. Then you shrink the triangle by half in terms of height and width and make three copies. These copies are positioned so that each triangle touches the two other triangles at a corner. You keep repeating this until all the required levels are complete (if possible).

You can read more about Sierpinski triangles [here.](https://en.wikipedia.org/wiki/Sierpiński_triangle) 

To get my code:  

[Sierpinski Triangles](https://github.com/MarkGadsby/TurtleGraphics/blob/master/RecursiveTriangles/SierpinskiTriangles.py)

1. Look at the line that calls the function `SierpinskiTriangles()` and experiment with the second two arguments.
2. Run the code with the second argument set to 0, than 1, 2 and so on. This shows the effect of increasing the depth.
3. Fun can also be had changing the fill color and line color and width.


[Home](https://github.com/MarkGadsby/TurtleGraphics/wiki)
