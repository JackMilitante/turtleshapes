#playing with turtle graphics
#by @jack

import turtle

#create window
loadWindow = turtle.Screen()
loadWindow.title("Test Turtle")
# loadWindow.setup(width=800, height=600)

#turn off draw mode
turtle.speed(0)
turtle.colormode(255)


#create and run turtles
def shape(size,sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

for i in range(10000000):
    shape(i, i)
    turtle.left(i)

#wait for user to exit
turtle.exitonclick()