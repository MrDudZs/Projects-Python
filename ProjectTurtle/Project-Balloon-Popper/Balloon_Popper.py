# Ballon Popper Game
# =============================================
# A simple balloon popper game!
# when balloon reaches 100px it goes "POP!"
# =============================================

from turtle import *

# ==================
#    Variables
# ==================

diameter = 40
pop_diameter = 300

# ==================
#    Functions
# ==================

# Creates Balloon
def draw_balloon ():
    color("Red")
    dot(diameter)

# Inflates Balloon
def inflate_balloon ():
    global diameter
    diameter = diameter + 25
    draw_balloon()
    
    # Destroys balloon
    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!")


draw_balloon() # Starts project

# ==================
#      Inputs
# ==================
onkey(inflate_balloon, "Up")

listen() # Reads key presses

done()