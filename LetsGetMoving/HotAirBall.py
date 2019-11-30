from turtle import Turtle, Screen

window = Screen()

window.setup(800,600)
window.bgcolor("cornflowerblue")
# Ball
ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("red")
ball.shapesize(1)
ball_radius = 10       # Save the new radius for later
ball_move_horiz = 0    # Horizontal movement per frame
ball_move_vert  = 4    # Vertical movement per frame

def update_ball_position():
    global ball_move_vert, ball_move_horiz
    ball.setx(ball.xcor() + ball_move_horiz)
    ball.sety(ball.ycor() + ball_move_vert)
    
def frame ():
    update_ball_position()
    window.update()                      # show the new frame
    window.ontimer(frame, framerate_ms)  # schedule this function to be called again a bit later

framerate_ms = 10 # Every how many milliseconds must frame function be called?
frame()


