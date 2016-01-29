

import turtle
wn = turtle.Screen()
alice = turtle.Turtle()


def sqSpiral():
    sideLen = eval(input("Beginning Length:")) #starting side length, will also act as accumulator
    chgLen = eval(input("Change in Length:"))
    numSides = eval(input("Number of sides to draw:"))
    if chgLen < 0: #If it's an inward spiral, move so that it appears in center of screen. 
        reposition(sideLen) #(Outward spirals automatically start from center, unless repositioned by user.) 
    for i in range(numSides):
        alice.lt(90)
        alice.fd(sideLen)
        sideLen += chgLen  #increase or decrease side length using pos/neg chgLen

    
def reposition(maxWidth):
    halfDist = maxWidth/2 
    alice.pu()
    alice.fd(halfDist) #go half the width of future spiral to the right
    alice.rt(90)
    alice.fd(halfDist) #and half the width down
    alice.lt(90)
    alice.pd()   #then put down pen and point in correct direction. 


def spiral(startRadius, changeFactor, times): #I made a circular spiral for fun!
    times *= 6
    times = int(times)
    for i in range(times):
        alice.circle(startRadius +(i*changeFactor),60)

