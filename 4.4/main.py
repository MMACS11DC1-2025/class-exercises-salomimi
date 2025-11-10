# Title:
# Author: Salomi Aiyathurai

import turtle

recursive_drawings = {
    "tree": {}
    "snowflake": {}
}

themes = {
    # tree themes
    "original_tree": {"branch": "brown", "leaf": "green"}
    "red": {"light red": "#FFA07A", "dark red": "#8B0000"}
    "orange": {"light orange": "#FFD580", "dark orange": "#FF8C00"}
    "yellow": {"light yellow": "#FFFF99", "dark yellow": "#FFD700"}
    "green": {"light green": "#90EE90", "dark green": "#006400"}
    "brown": {"light brown": "#CF8E39", "dark brown": "#8B4513"}

    # snowflake themes
    "original_snowflake": {"light gray": "#E0E0E0", "dark gray": "#404040"}
    "icy": {"light blue": "#E0FFFF", "dark blue": "#1E90FF"}
    "frost": {"light frost": "#F0F8FF", "dark frost": "#4682B4"}
}

def drawTree(level, branchLength, angle, colors):
    if level > 0:
        # dark colors are branches
        turtle.color(list(color.values())[1]) 
        turtle.forward(branchLength)
        turtle.left(angle)
        drawTree(level - 1, branchLength / 1.6, angle, colors)
        turtle.right(angle * 2)
        drawTree(level - 1, branchLength / 1.6, angle, colors)
        turtle.left(angle)
        turtle.backward(branchLength)
    else:
        # light colors for leaves
        turtle.color(list(colors.values())[0]) 
        turtle.stamp()

def snowflake(length, level, color):
    turtle.color(color)
    if level == 0:
        turtle.forward(length)
        return
    length = length / 3.0
    snowflake(length, level - 1, color)
    turtle.left(60)
    snowflake(length, level - 1, color)
    turtle.right(120)
    snowflake(length, level - 1, color)
    turtle.left(60)
    snowflake(length, level-1, color)

def drawSnowflake(length, level, colors):
    # uses dark colors
    turtle.color(list(colors.values())[1])
    for i in range(3):
        # uses light colors
        snowflake(length, level, list(colors.values())[0])
        turtle.right(120)

print("Choose which drawing you want!")
print("Print 1, if you want me to draw you a tree")
print("Print 2, if you want me to draw you a snowflake")

drawing_choice = input("Enter 1 or 2: ")
while drawing_choice not in ["1", "2"]:
   drawing_choice = input("Invalid input. Please enter 1 or 2: ") 

print("You chose option number " + drawing_choice)