[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  
[Colour Swatch](https://social.technet.microsoft.com/wiki/contents/articles/23237.small-basic-getting-started-guide-appendix-b-colors.aspx)

# Turtle Graphics with Python

We are now ready to draw our snowflakes.

## Drawing a snowflake

Just like a flower is made up of petals a snowflake is made up of *branches*. But also branches are made up of splays like this:

![Splay](./Images/SnowflakeSplay.png)

The code for it is here for you:
[Splay code](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/Splay.py)

Then we can line up these splays to form a **branch** like this:

![Branch](./Images/SnowflakeBranch.png)

Here is the code for it:
[Branch code](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/Branch.py)

If we put the branch drawing code inside a `for` loop we can draw 8 branches and rotate by 45 degrees each time.

This means we complete a full circle because 8 times 45 is 360 degrees, a full circle.

![Snowflake](./Images/Snowflake.png)  

The code for the Snowflake is [here](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/SnowFlake.py)

I than moved the code for drawing a single snowflake to a function called `DrawSnowflake()`. This function will call the`randint` function from the `random` library to generate a number of branches between 4 & 30. So each time we call `DrawSnowflake()` we get a different looking snowflake. See the code [here.](https://github.com/MarkGadsby/TurtleGraphics/blob/master/SnowFlakes/SnowFlakes.py)

![Snowflakes](./Images/Snowflakes.png)  

[Home](https://github.com/MarkGadsby/TurtleGraphics/wiki)
