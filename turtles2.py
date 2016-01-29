
import turtle
wn = turtle.Screen()
alice = turtle.Turtle()

def offset(size, times):
    alice.pu()
    reverseDist = (size*times)/2
    alice.bk(reverseDist)
    alice.pd()

def square(size):
    for i in range(4):
        alice.fd(size)
        alice.rt(90)

def ladder(times):
    for i in range(times):
        square(50)
        alice.fd(50)

def fillSquare(size, pencolor, fillColor):
    alice.color(pencolor, fillColor)
    alice.begin_fill()
    square(size)
    alice.end_fill()

def colorLadder(size, times, ps, color1, color2, color3, penColor):
    offset(size, times)
    alice.pensize(ps)
    for i in range(times):
        colorNum = i%3
        if (colorNum==0):
            fill = color1
        elif (colorNum == 1):
            fill = color2
        else:
            fill = color3
        fillSquare(size, penColor, fill)
        alice.fd(size)
    offset(size, times)#re-center Alice
  
    
def corner(size):
    alice.pu()
    alice.bk(size/2)
    alice.lt(90)
    alice.bk(size/2)
    alice.pd()

def center(size): #starting in lt corner...
    alice.pu()
    alice.fd(size/2)
    alice.rt(90)
    alice.fd(size/2)
    alice.pd()

def centeredBoxes(size, times, factor):
    for i in range(times):
        corner(size)
        square(size)
        center(size)
        size *= factor
    

def centeredBoxes2(size, times, delta):
    for i in range(times):   
        corner(size)
        square(size)
        center(size)
        size += delta 

##def cntrdSquares(startSize, times):
##    size = startSize
##    for i in range(times):
        

'''Breaks today: 9-1pm --> 4hrs
3-6pm --> 2hrs '''

