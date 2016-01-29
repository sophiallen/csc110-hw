

import random

##for i in range(20):
##    n = random.randrange(1, 4)
##    print(n, end = ' ')

    
import turtle
wn = turtle.Screen()
alice = turtle.Turtle()

def randIntsOnLine():
    for i in range(15):
        n = random.randrange(-2, 3)
        print(n, end=' ')



def randomWalk(s, times):
    for i in range(times):
        colorNum = i%3
        alice.pensize(4)
        if colorNum == 0:
            alice.color('red')
        elif colorNum == 1:
            alice.color('blue')
        else:
            alice.color('green')
        turn = random.randrange(-360, 360)
        distance = random.randrange(-50, 50)
        alice.lt(turn)
        alice.fd(s)


def randomWalkBorder(s, radius):
    alice.circle(radius)
    alice.lt(90)
    alice.fd(radius)
    print(alice.position())
    

        
        
