# ==============================================================
# Using Random & Turtle to create a "Stars" background at random
# ==============================================================

from random import *
from turtle import *

# ==================
# Project Settings
# ==================

# Background colour
bgcolor("Black")

# Hides turtle
hideturtle()

# Sets speed
speed(0)

# Detects width & height
width = window_width()
height = window_height()

# ==================
# Functions
# ==================

# Sets Positon & Size of stars
def draw_star (xpos, ypos): # "Xpos" = X Axis "ypos" = Y Axis
    size = randrange(1, 10) # Sets star size from 1 - 10
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "White")

# Creates stars
for x in range(500):
    # Creates a random x & y position
    xpos = randrange(-width, width)
    ypos = randrange(-height, height)
    
    # Starts Project
    draw_star(xpos, ypos)

done()
