
import turtle
wn = turtle.Screen()

alice = turtle.Turtle()


def dashes(size, numDashes):
    for i in range(numDashes):
        alice.forward(size)
        alice.pu()
        alice.forward(size)
        alice.pd()
        
def flower(size):
    for i in range(5):
        alice.circle(size)
        alice.left(72)

def dahlia(size, flwrColor):
    alice.pensize(4)
    alice.color(flwrColor)
    flower(size)
    alice.right(36)
    flower(size)
    
def wave():
    for i in range(10):
        alice.circle(50-(i*10), 75)
        

def spiral():
    for i in range(20):
        alice.circle(100-(i*5), 65)

