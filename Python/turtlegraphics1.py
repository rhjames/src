import math
import turtle

print"Lets draw some lines!  This program will intake 2 sets of coordinates and draw lines"
onex = float(raw_input("Please enter a first X coordinate "))
oney = float(raw_input("Please enter a first Y coordinate "))
twox = float(raw_input("Please enter a second X coordinate "))
twoy = float(raw_input("Please enter a second Y coordinate "))

turtle.up()
turtle.goto(onex,oney)
turtle.down()
turtle.goto(twox,twoy)
turtle.goto(360,56)
turtle.up()
turtle.goto(240,178)
turtle.down()
turtle.goto(120,178)
turtle.write("I'm doing it!")
turtle.done()

slope_one = (twoy - oney) / (twox - onex)


print slope_one