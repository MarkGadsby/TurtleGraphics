[Python Turtle Help](https://docs.python.org/3.8/library/turtle.html#module-turtle)  
[Colour Swatch](https://social.technet.microsoft.com/wiki/contents/articles/23237.small-basic-getting-started-guide-appendix-b-colors.aspx)

# Turtle Graphics with Python

## Introducing animation

All animation (indeed, all moving pictures) is fundamentally nothing more than consecutive pictures being shown so quickly that it simulates continuous motion. Each picture is called a frame. Each frame must differ from the previous one slightly, and quickly showing the frames one after the other gives the illusion of continuous motion, hence the word ‘animate’ as in ‘bring to life’. The frames have to be shown at a rate of about 12 or more frames per second (fps) for a person to experience them as an animation. Modern film generally uses 24 frames per second.

![Running horse](./Images/The_Horse_in_Motion_high_res.jpg)  

If we call `Screen.tracer()` we can take control of drawing the screen. We can then call `Screen.update()` when we want to redraw to the screen. This can be taken a little further by using the `Screen.ontimer()` function which allows us to define a `frame()` function which will be called every few milliseconds. Just like running a film.

But first lets get a ball on the screen, see the code [here, Ball on screen](https://github.com/MarkGadsby/TurtleGraphics/blob/master/LetsGetMoving/BallOnScreen.py)

We can make it look like the ball is filled with helium if we add call to new function called `update_ball_position()` every frame.  

[Helium Ball](https://github.com/MarkGadsby/TurtleGraphics/blob/master/LetsGetMoving/HotAirBall.py)

Experiment with the variables called ball_move_vert and framerate_ms, can you make the ball rise more smoothly?

![Falling ball](./Images/FallingBall.png)  

Given that we know the coordinates of the screen and ball we can add some code to bounce the ball off the top and bottom of the screen, see the [code here](https://github.com/MarkGadsby/TurtleGraphics/blob/master/LetsGetMoving/UpDownBounce.py)

Can you add movement in the horizontal direction as well?

[Home](https://github.com/MarkGadsby/TurtleGraphics/wiki)
