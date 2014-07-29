__author__ = 'ada'

import random
import turtle

def tree(branchLen,width,t):
    print "apelat tree " + str(branchLen)
    if branchLen > 5:
        t.width(width)
        if branchLen == 15:
            t.color("red")
        t.forward(branchLen)
        t.right(20)

        if width > 5:
            newWidth = width - 5
        else:
            newWidth = 1
        tree(branchLen-(random.randrange(5,25)), newWidth,t)
        t.left(40)
        tree(branchLen-(random.randrange(5,25)), newWidth,t)
        t.right(20)
        t.backward(branchLen)
        t.color("green")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,20,t)
    myWin.exitonclick()

main()


