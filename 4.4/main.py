# Title:
# Author: Salomi Aiyathurai

# importing the turtle module
import turtle

# cretaing a turtle object and giving the turtle name
turtle = turtle.Turtle()

turtle.speed(0)
turtle.penup()      # gets the pen up so it doesn't start drawing it tries to get to the sarting point 
turtle.left(90)     # makes the turtle face upward or the right way

# dictionary holds the parameters for the tree drawing
recursive_drawing = {
    "tree": {
        "angle": 25,"branchLength": 100
    }
}

# syntax error: forgot to put commas between each entery in dictionary
# dictinary for the different color themes 
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
        turtle.color(list(colors.values())[1]) 
        # draws one branch forward which is the trunk
        turtle.forward(branchLength)
        # draws the left branch
        turtle.left(angle)
        left_branch = drawTree(level - 1, branchLength / 1.6, angle, colors)
        # turns twice as much and draw another branhc which is the right branch
        turtle.right(angle * 2)
        right_branch = drawTree(level - 1, branchLength / 1.6, angle, colors)
        turtle.left(angle)
        turtle.backward(branchLength)
        # return the number of recursive calls
        return 1 + left_branch + right_branch
    
    else:
        # light colors for leaves
        turtle.color(list(colors.values())[0]) # list colors?
        turtle.stamp()      # stamps leaf shape
        return 1            # one recursive call 

# starting x position for the first tree
next_tree_x = -200

# varibale for total recursive calls from all tree (global variable)
total_recursive_calls = 0

# runs till user decides to exit (2)
while True:
    # program is asking user to draw a tree or exit the program
    choice = input("Enter 1 if you want a tree, 2 if u don't want to continue: ")

    # the program make sures the user picks "1" or "2", it uses the while loop to make sure they input 1 or 2, if they input something that isnt 1 or 2 the program would ask them to input 1 or 2
    while choice not in ["1", "2"]:
        choice = input("Invalid input. Please enter 1 or 2: ") 

    # if user chooses to quit
    if choice == "2":
        print("Bye, the code has ended!")
        print("Total recursive calls made in total:" + str(total_recursive_calls))
        break
    
    # asks user for color theme choice
    print("Choose a tree color theme:")
    print("original, red, orange, yellow, green, brown")
    theme_choice = input("Enter theme: ").lower()

    # make sure its a valid color theme input
    while theme_choice not in tree_themes:
        theme_choice = input("Invalid input, enter a theme: ").lower()
    
    # gets the selected color theme
    theme = tree_themes[theme_choice]

    # akss user what level they wat 
    level = int(input("Enter how many levels of the drawing you want: "))

    # prevents the code from doign a very high level which takes a while to do
    if level > 50:
        print("Too much to print.")
        exit()
    
    # move turtle to nect tree position
    turtle.penup()
    turtle.goto(next_tree_x, -180)
    turtle.right(90)        # adjusts it agian before drawing
    turtle.left(90)
    turtle.pendown()
    
    # draws the tree & ocunt recursive calls
    calls = drawTree(level, recursive_drawing["tree"]["branchLength"], recursive_drawing["tree"]["angle"], theme)
    
    # add to total recurisve calls
    total_recursive_calls += calls

    # move the next trees postion 
    next_tree_x += 250
