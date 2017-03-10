
import turtle
import time
import random


# let's start up a Turtle Graphics window with a red turtle (pen)
turtle.color(1,0,0)

# prompt before starting to draw
print("Look for the Python Turtle Graphics window")

print("Position it and the Python Shell window side by side.")

# put it down so all movement will show as a (red) line (until we change colors)
turtle.down()
# move forward by 100 (in direction that turtle points in, initially (0,1)
turtle.forward(100)
# rotate direction of turtle by 120 degrees
turtle.right(120)
# change the color to green
turtle.color(0,1,0)
# move forward by 100 (in direction that turtle points in, initially (0,1)
turtle.forward(100)
# rotate direction of turtle by 120 degrees
turtle.right(120)
# change the color to blue
turtle.color(0,0,1)
# move forward by 100 (in direction that turtle points in, initially (0,1)
turtle.forward(100)
# rotate direction of turtle back to its start rotation
turtle.right(120)

# to go to a new location without drawing any line
turtle.up()
turtle.goto(0, 50)

# change the pen color to a random color
turtle.color(random.random(),random.random(), random.random())
# lower the pen
turtle.down()

# this time, we'll draw a filled triangle going up
turtle.begin_fill()
turtle.forward(100)
turtle.right(-120)
turtle.forward(100)
turtle.right(-120)
turtle.forward(100)
turtle.end_fill()

    
turtle.hideturtle()

turtle.done()