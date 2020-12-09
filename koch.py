"""
Author: Justin Park and Harry Pinkerton
Project 7
File: koch.py

Draws the Koch snowflake.
"""

from turtle import Turtle, tracer, update
import sys

def drawFractalLine(t, length, level):
    """Draw the Koch snowflake given length and level"""
    if level == 0:
        t.forward(length)
    else:
        level-=1
        length=length/3
        drawFractalLine(t, length, level)
        t.left(60)
        drawFractalLine(t,length,level)
        t.right(120)
        drawFractalLine(t,length,level)
        t.left(60)
        drawFractalLine(t,length,level)

def main():
    # Get the level from the command line argument
    if len(sys.argv) == 1:
        level = 0
    else:
        level = int(sys.argv[1])
    if level > 6:
        tracer(False)
    t=Turtle()
    t.speed(0)
    t.hideturtle()
    t.pencolor("blue")
    drawFractalLine(t,200,level)
    t.right(120)
    drawFractalLine(t,200,level)
    t.right(120)
    drawFractalLine(t,200,level)
    t.right(120)
    if level > 6:
        update()
    # Stop the fly-by window in the terminal
    input("Press enter to quit: ")
    
if __name__ == "__main__":
    main()
