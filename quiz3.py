
import turtle
wn = turtle.Screen()
alice = turtle.Turtle()

def triangle(sz):
    for i in range(3):
        alice.fd(sz)
        alice.lt(120)

def reposition(sz):
    dist = sz/3
    alice.pu()
    alice.fd(dist)
    alice.rt(60)
    alice.fd(dist)
    alice.lt(120)
    alice.pd()

def star(sz):
    triangle(sz) #first triangle
    reposition(sz)
    triangle(sz)

    
    
        
    
