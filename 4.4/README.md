### **Documentation & Process**
- [ ] README.md file with project documentation explaining the approach used and how to use the program (2 pts)
## Project overrevieq
- This code uses turtle graphic's and recursion to draw recursive trees.
- Every time a user runs the program they can decide to draw a tree if they want, how many levels of branches, select which color theme they want, at the end when the user wants to stop runnign the code it will print out how many recursive calls we did in total.
- it shows recursion by callin the drawTree() function multiple times to draw smaller branches till the base case is met

## How it works
1. the program starts by importing the turtle function
2. the program gives thigns where the user needs to input:
    - it asks gthe user to draw a tree (1) or quit/exit the program (2)
    - if the user decides to draw a tree, then the program asks which color theme it wants fromt he options
    - then they are aked about how many recursive levels they wnat the tree to have
3. the function drawTree() draws thr truck and a branch everytime its called
    - the base case is when level == 0, whcih draws like leaves and stops the recursion
4. the function returns how many recursive calls(calls) were made, which adds to the tottal (total_recursive_calls)
5. when the user quits or exits (2), the total number of recursive calls for all trees is shown

## hwo it runs
1. use main.py 
2. run it in trinker
3. do the prompts that is given by the program:
    - type 1 to get the program to draw a tree
    - choose a color theme
    - enetr a recursion level
    - type 2 when u want the program to stop making trees

## test cases
1. - input: 1 -> theme = "original", level 3
    - xpected output: small tree, few branches
    - actual output: what i thought was gonna output

2. - input: 1 -> theme = "green", level 5
    - xpected output: small tree, few branches more than level 3 in text case 1
    - actual output: what i thought was gonna output

3. - input: 1 -> theme = "green", level 5
    - xpected output: small tree, few branches more than level 3 in text case 1
    - actual output: what i thought was gonna output








- [ ] Code must be well commented to enhance readability (2 pts)
- [ ] Test cases with expected vs actual results (2 pts)
- [ ] Screenshots of visual outputs for each test case (2 pts)
- [ ] Discussion of reasonable recursion depth (for your program, what depth is too low, what is too high, and why?) (2 pts)
- [ ] Documentation of debugging and testing process in README.md (2 pts)
- [ ] Source code is committed to repository on Github with **at least 3 meaningful commits on different days** (2 pts