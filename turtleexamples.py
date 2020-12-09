"""
Author: Justin Park and Harry Pinkerton
Project 7
File: turtleexamples.py

Defines some functions to draw geometric shapes in turtle graphics.
"""

import random
from turtle import Turtle

def drawSquare(t, length):
    """Draws a square with length."""
    for count in range(4):
        t.forward(length)
        t.left(90)

def drawPentagon(t, length):
    """Draws a pentagon with length."""
    for count in range(5):
        t.forward(length)
        t.left(72)

def drawFlower(t, length, s=4,shape=drawSquare):
    """Draws a flower with length."""
    for petals in range(s):
        shape(t, length)
        t.left(360/s)
        
def drawPolygon (t, length, n):
    """Draws a polygon"""
    for count in range(n):
        t.forward(length)
        t.left(360/n)

def fillRectangle(t, x1, y1, x2, y2):
    """Draws and fills a rectangle with the given corner points in a random color"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()
# Microprogram to test functions

def main():
    """This is run only when F5 is pressed from IDLE or when
    this file is run as a script in a terminal window."""
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("blue")
    
    drawSquare(t, 50)
    drawPentagon(t, 50)
    drawFlower(t, 50)
    for sides in range(3, 7):     # Draw triangle, square, pentagon, hexagon
        drawPolygon(t, 50, sides)
    drawPolygon(t, 50, 8)                 # Draw octagon
    drawFlower(t, 50)                   # Flower with 4 squares
    drawFlower(t, 50, 10)               # Flower with 10 squares
    drawFlower(t, 50, 6, drawPentagon)  # Ditto
    drawFlower(t, 50, 4, lambda t, length: drawPolygon(t, length, 8)) # 4 octagons
    fillRectangle(t,20,50,80,100)
    
if __name__ == "__main__":
    main()
