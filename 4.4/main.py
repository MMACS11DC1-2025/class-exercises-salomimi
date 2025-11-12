# Title:
# Author: Salomi Aiyathurai

import turtle

recursive_drawings = {
    "tree": {
        "angle": 25,
        "branchLength": 100
    },
    "snowflake": {
        "length": 200
    }
}

# syntax error: forgot to put commas between each entery in dictionary
tree_themes = {
    # tree themes
    "original tree": {"leaf": "green", "branch": "brown"},
    "red": {"light red": "#FFA07A", "dark red": "#8B0000"},
    "orange": {"light orange": "#FFD580", "dark orange": "#FF8C00"},
    "yellow": {"light yellow": "#FFFF99", "dark yellow": "#FFD700"},
    "green": {"light green": "#90EE90", "dark green": "#006400"},
    "brown": {"light brown": "#CF8E39", "dark brown": "#8B4513"}
}

snowflake_themes = {
    # snowflake themes
    "original snowflake": {"light gray": "#E0E0E0", "dark gray": "#404040"},
    "icy": {"light blue": "#E0FFFF", "dark blue": "#1E90FF"},
    "frost": {"light frost": "#F0F8FF", "dark frost": "#4682B4"}
}

def drawTree(level, branchLength, angle, colors):
    if level > 0:
        # dark colors are branches
        turtle.color(list(colors.values())[1]) # list colors?
        turtle.forward(branchLength)
        turtle.left(angle)
        drawTree(level - 1, branchLength / 1.6, angle, colors)
        turtle.right(angle * 2)
        drawTree(level - 1, branchLength / 1.6, angle, colors)
        turtle.left(angle)
        turtle.backward(branchLength)
    else:
        # light colors for leaves
        turtle.color(list(colors.values())[0]) # list colors?
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
    turtle.color(list(colors.values())[1]) # list colors?
    for i in range(3):
        # uses light colors
        snowflake(length, level, list(colors.values())[0]) # list colors?
        turtle.right(120)

# asking user which drawing they want the program to draw
print("Choose which drawing you want!")

# if they pick 1 then the program is drawing a tree
print("Print 1, if you want me to draw you a tree")

# if they pick 2, then the program is drawing a snowflake
print("Print 2, if you want me to draw you a snowflake")

# program is asking user to input 1 or 2 
drawing_choice = input("Enter 1 or 2: ")

# the program make sures the user picks 1 or 2, it uses the while loop to make sure they input 1 or 2, if they input something that isnt 1 or 2 the program would ask them to input 1 or 2
while drawing_choice not in ["1", "2"]:
   drawing_choice = input("Invalid input. Please enter 1 or 2: ") 

print("You chose option number " + drawing_choice)

if drawing_choice == "1":
    print("Choose a tree color theme:")
    print("original tree, red, orange, yellow, green, brown")
    theme_choice = input("Enter theme: ").lower()

    while theme_choice not in tree_themes:
        theme_choice = input("Invalid input, enter a theme: ").lower()

    theme = tree_themes[theme_choice]

else:
    print("Choose a snowflake color theme:")
    print("original snowflake, frostfrost, icy")
    theme_choice = input("Enter theme: ").lower()

    while theme_choice not in snowflake_themes:
        theme_choice = input("Invalid input, enter a theme: ").lower()

    theme = snowflake_themes[theme_choice]

level = int(input("Enter how many levels of the drawing you want: "))
if level > 50:
    print("Too much to print.")
    exit()

turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)

if drawing_choice == "1":
    turtle.goto(0, -180)
    turtle.left(90)
    turtle.pendown()
    drawTree(level, recursive_drawings["tree"]["branchLength"], recursive_drawings["tree"]["angle"], theme)

else:
    turtle.pendown()
    drawSnowflake(recursive_drawings["snowflake"]["length"], level, theme)

turtle.done()