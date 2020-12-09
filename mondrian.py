"""
Author: Justin Park and Harry Pinkerton
Project 7
FIle: mondrian.py

This program displays a Mondrian-like painting with 
the user's input level.  The program obtains the level 
from a command-line argument.  Thus, python3 mondrian.py 6
draws a painting at level 6.
"""

import random
import sys
from turtle import Turtle, tracer, update
from turtleexamples import fillRectangle

def drawRectangle(t, x1, y1, x2, y2):
    """Draws and fills a rectangle with the given corner points
    in a random color."""
    fillRectangle(t,x1, y1, x2, y2)



def mondrian(t, x1, y1, x2, y2, level):
    """Draws a Mondrian painting at the given level."""
    if level > 0:
        drawRectangle(t, x1, y1, x2, y2)

        vertical = random.randint(1, 2)
   
        if vertical == 1:   # Vertical split
            up = random.randint(1,2)
            if up == 1:    
                mondrian(t, x1, y1, (x2 - x1) / 3 + x1, y2,
                     level - 1)
                mondrian(t, (x2 - x1) / 3 + x1, y1, x2, y2, 
                     level - 1)
            else:
                mondrian(t, x1, y1, 2 * (x2 - x1) / 3 + x1, y2,
                     level - 1)
                mondrian(t, 2 * (x2 - x1) / 3 + x1, y1, x2, y2, 
                     level - 1)

        else:               # Horizontal split
            left = random.randint(1,2)
            if left == 1:
                mondrian(t, x1, y1, x2, (y2 - y1) / 3 + y1, 
                     level - 1)
                mondrian(t, x1, (y2 - y1) / 3 + y1, x2, y2, 
                     level - 1)
            else:
                mondrian(t, x1, y1, x2, 2 * (y2 - y1) / 3 + y1, 
                     level - 1)
                mondrian(t, x1, 2 * (y2 - y1) / 3 + y1, x2, y2, 
                     level - 1)

def main():
    # Get the level from the command line argument
    if len(sys.argv) == 1:
        level = 1
    else:
        level = int(sys.argv[1])
    if level > 6:
        tracer(False)
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    x = t.screen.window_width() // 2 - 20
    y = t.screen.window_height() // 2 - 20
    mondrian(t, -x, y, x, -y, level)
    if level > 6:
        update()
    # Stop the fly-by window in the terminal
    input("Press enter to quit: ")

if __name__ == "__main__":
    main()
