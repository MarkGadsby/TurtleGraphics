[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  
[Colour Swatch](https://social.technet.microsoft.com/wiki/contents/articles/23237.small-basic-getting-started-guide-appendix-b-colors.aspx)

# Turtle Graphics with Python

Before we write our snowflakes lets start by thinking about drawing a flower with a variety of petals.

## Drawing a flower

The first thing a flower needs is petal like this one: 
 
![Petal](./Images/Petal.png)

The code for it here:
[Petal code](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/Petal.py)

It is a bit like the drawing an offset square, can you see how the shape is drawn in two halves?

If I put the petal drawing code inside another `for` loop we can draw 10 petals and rotate by 36 degrees each time.

This means we complete a full circle because 10 times 36 is 360 degrees, a full circle.

![Flower](./Images/Flower.png)  

The code for the flower is [here,](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/Flower.py) you can see how I have placed all the flower drawing code in its own function called `DrawFlower()`  


Remember how we worked out the 360 degree rotation? The amount of rotation is just the number of petals divided by 360. This means we can add a parameter to `DrawFlower()` called nPetals like this, `DrawFlower(nPetals).` nPetals is the number of petals we would like. We can also use the `setpos()` turtle function to move to various positions on the screen.

![VariousPetals](./Images/RandomPetals.png)  

The code for this is [here.](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/FlowerVariousPetals.py) Experiment with setting different numbers of petals each time you call `DrawFlower`

The final change to this code in this section to make the number of petals random. For this we can use the `randint` function from the `random` library. In each call to `DrawFlower(nPetals)` we pass in a new random number between two values.

![RandomPetals](./Images/VariousPetals.png)  

The final code is here:

[Flowers with random petals](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/FlowerRandomPetals.py)

Now we are ready to bring in new functions to draw snowflakes with random dimensions.

[Next, Snowflakes](https://github.com/MarkGadsby/TurtleGraphics/wiki/SnowFlakes)

[Home](https://github.com/MarkGadsby/TurtleGraphics/wiki)
