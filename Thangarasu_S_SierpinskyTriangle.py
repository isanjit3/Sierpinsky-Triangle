"""
Sanjit Thangarasu
Period 7 | Block A | Mr. Gordon
Sierpinski Triangle Recursion Model
This is a program that takes two (2) user inputs, the base length of the triangle,
as well as the degree to which the program should execute the program.
"""

#import turtle module and random module
import turtle, random
#import 'square root' function from math module
from math import sqrt
wn = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()

"""
The purpose of this function is mainly to set the direction and position of the turtle,
draws the base with user inputted length
"""
def drawLine(x, y, length, angle):
    t.up()
    """
    rather than turning the turtle head to a certain angle, the 'setheading' function
    sets it to a specific direction on an imaginary circle with 0 = east, 90 = north, 180 = west, and 270 = south
    """
    t.setheading(angle)
    #goes to bottom left corner
    t.goto(x, y)
    t.down()
    t.fd(length)


"""
this function is in charge of drawing all of the triangles inside the main triangle
"""
def drawTriangle(x, y, length):
    t.up()
    R = random.random()
    G = random.random()
    B = random.random()
    t.color(R, G, B)

    t.begin_fill()
    drawLine(x, y, length, 60)
    drawLine(x + length/2, y + (length/2) * sqrt(3), length, 300)
    drawLine(x + length, y, length, 180)
    t.end_fill()


"""
This function finds the mids for the triangles
"""
def findMid(x, y, length):
    t.up()
    t.color("White")
    t.begin_fill()
    drawLine(x, y, length, 60)
    drawLine(x + length/2, y + (length/2) * sqrt(3), length, 180)
    drawLine(x - length/2, y + (length/2) * sqrt(3), length, 300)
    t.end_fill()


def sierpinski(x, y, length, degree):
    t.up()
    if degree <= 0:
        t.up()
        #print("Please try again with a degree greater than 0")
        #writeText()
        return

    drawTriangle(x, y, length)

    if degree > 1:
        findMid(x + length/2, y, length/2)

    sierpinski(x, y, length/2, degree-1)
    sierpinski(x + length/2, y, length/2, degree-1)
    sierpinski(x + length/4, y + (length/4)*sqrt(3), length/2, degree-1)

def writeText():
    t.up()
    t.goto(0, -((2*length/5)*sqrt(3)))
    t.down()
    t.color("Black")
    t.write("Sanjit Thangarasu Block A | Sierpinski Triangle to degree "+ str(degree), font=("Times New Roman", 25), align="center")

def main():
    #Gets user input for length and degree for the triangle
    global length, degree

    length = int(input("Enter a length for the base of the Triangle: "))
    degree = int(input("Enter a degree to which the program will execute: "))

    turtle.delay(0)
    sierpinski(-length/2, -length/2, length, degree)

main()

writeText()

turtle.exitonclick()
