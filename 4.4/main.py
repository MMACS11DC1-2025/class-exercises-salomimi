# Title:
# Author: Salomi Aiyathurai

import turtle
turtle = turtle.Turtle()
turtle.speed(0)
turtle.penup()

recursive_drawings = {
    "tree": {
        "angle": 25,"branchLength": 100
    }
}

# syntax error: forgot to put commas between each entery in dictionary
tree_themes = {
    # tree themes
    "original": {"leaf": "green", "branch": "brown"},
    "red": {"light red": "#FFA07A", "dark red": "#8B0000"},
    "orange": {"light orange": "#FFD580", "dark orange": "#FF8C00"},
    "yellow": {"light yellow": "#FFFF99", "dark yellow": "#FFD700"},
    "green": {"light green": "#90EE90", "dark green": "#006400"},
    "brown": {"light brown": "#CF8E39", "dark brown": "#8B4513"}
}

def drawTree(level, branchLength, angle, colors):
    if level > 0:
        # dark colors are branches
        turtle.color(list(colors.values())[1]) # list colors?
        turtle.forward(branchLength)
        turtle.left(angle)
        left_branch = drawTree(level - 1, branchLength / 1.6, angle, colors)
        turtle.right(angle * 2)
        right_branch = drawTree(level - 1, branchLength / 1.6, angle, colors)
        turtle.left(angle)
        turtle.backward(branchLength)
        return 1 + left_branch + right_branch
    
    else:
        # light colors for leaves
        turtle.color(list(colors.values())[0]) # list colors?
        turtle.stamp()
        return 1

while True:
    # program is asking user to input 1 or 2 
    choice = input("Enter 1 if you want a tree, 2 if u don't want to continue: ")

    # the program make sures the user picks 1 or 2, it uses the while loop to make sure they input 1 or 2, if they input something that isnt 1 or 2 the program would ask them to input 1 or 2
    while choice not in ["1", "2"]:
        choice = input("Invalid input. Please enter 1 or 2: ") 

    if choice == "0":
        print("Bye, the code has ended!")
        break
    
    print("Choose a tree color theme:")
    print("original, red, orange, yellow, green, brown")
    theme_choice = input("Enter theme: ").lower()

    while theme_choice not in tree_themes:
        theme_choice = input("Invalid input, enter a theme: ").lower()
    theme = tree_themes[theme_choice]

    level = int(input("Enter how many levels of the drawing you want: "))
    if level > 50:
        print("Too much to print.")
        exit()

    turtle.done()