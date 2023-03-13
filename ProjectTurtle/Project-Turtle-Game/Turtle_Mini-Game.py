# =================================
# Top down turtle game
# Made my MrDudZs (Matthew Dudley)
#==================================
from turtle import *
from random import *

# ==================
#      Settings
# ==================
# Background
bgcolor("#CBAE53")

# Draw speed
speed(0)

# Variables
move_distance = 20

# =====================
#   End Goal Creation
# =====================

# Puts pen to ocean area
penup()
goto(100, 200)
pendown()

# Ocean creation
color("LightBlue")
begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

# Obstical
color("Red")
begin_fill()
goto(100, 100)
goto(100, -100)
goto(100, -25)
goto(100, 25)
end_fill()

# ==================
#   Sprite Settings
# ==================

# Creates sprite

penup()
goto(-200, 0)
shape("turtle")
color("Green")

# ==================
#     Functions
# ==================

# Sets Movement directions
def move_up ():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down ():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left ():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right ():
    setheading(0)
    forward(move_distance)
    check_goal()

# Check to see if player has reached finish line
def check_goal ():
    if xcor() > 101:
        hideturtle()
        color("White")
        write("You WIN!")
        # Disables movement
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")
        clearscreen()
        Create_New()

def Create_New():
    bgcolor("#333")
    write("Well done!!!")
    penup()
    goto(randrange(-200, 0), randrange(-200, 0))
    shape("turtle")
    color("Green")
    onkey(move_up, "Up")
    onkey(move_down, "Down")
    onkey(move_left, "Left")
    onkey(move_right, "Right")
        
# ==================
#       Inputs
# ==================

onkey(move_up, "Up")

onkey(move_down, "Down")

onkey(move_left, "Left")

onkey(move_right, "Right")

listen()

done()