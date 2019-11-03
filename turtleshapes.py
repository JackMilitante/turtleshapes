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
    # shape(i, i)
    # turtle.left(i)
    turtle.circle(3*i)
    turtle.circle(-5*i)
    turtle.left(i)
    b=i
    if b > 51:
        b = 51
    turtle.color(i,2*i,5*b)


#wait for user to exit
turtle.exitonclick()