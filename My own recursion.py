#-------------------------------
# My Own Recursion
# Sydney Loerzel
# December 12, 19
#-------------------------------

import turtle

chim = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")

def tree(branch,chim):
    if branch > 1: #exit case, will keep calling while the branch length is longer than 1 
        chim.forward(branch) #go forward
        chim.right(20) #turn right
        tree(branch-10,chim) #makes a branch length of 10 units shorter of self
        chim.left(40) #turn left
        tree(branch-10,chim) #makes a branch length of 10 units short of calling self again
        chim.right(20) #turn right
        chim.backward(branch) #go backwards to the next branch

def main():
    chim.color("green")
    tree(60,chim) #call the first function
    chim.right(90)
    chim.color("white")
    tree(60,chim) #call the first function facing a different way
    chim.right(90)
    chim.color("blue")
    tree(60,chim)
    chim.right(90)
    chim.color("white")
    tree(60,chim) #repeated until a full circle is made
    wn.exitonclick()

main()