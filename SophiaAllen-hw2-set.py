
import math

#1. Zelle 3.1 - Sphere volume and Area
def sphereVolAndArea(radius):
    volume = (4/3) * math.pi * radius**3
    area = 4*math.pi*radius**2
    print('volume:', volume)
    print('area:', area)


#2. Zelle 3.5 Konditori Coffee
def orderCost(pounds):
    base = pounds * 10.5
    shipping = (pounds * .86) + 1.5
    total = base + shipping
    print('Order Total:', round(total, 2))

#3. Zelle 3.7 distance between 2 pts.
def distBtwPts(x1, y1, x2, y2):
    asq = (x2 - x1)**2
    bsq = (y2 - y1)**2
    dist = math.sqrt(asq + bsq)
    return dist


#4. Zelle 3.14 avg of numbers
def avgNums():
    totalNum = eval(input('How many numbers would you like to enter?: '))
    totalSum = 0
    for i in range(totalNum):
        num = eval(input('number, please: '))
        totalSum += num
    avg = totalSum/totalNum
    print("average:", avg)
    
#5. Zelle 3.15 approximates pi. Hint: Use sum accumulator to toggle +/-.
def approxPi():
    numTerms = eval(input("Number of terms to sum: "))
    piAccum = 0
    toggle = 1
    for i in range(1, numTerms*2, 2): 
        num = 4/(i) * toggle
        piAccum += num 
        toggle *= -1   
    print('Approximation:', piAccum)
    print('Difference from math.pi:', math.pi-piAccum)
    

#6. Write a function that takes 3 stick lengths and prints whether a triangle is possible.
def testTriangle(len1, len2, len3):
    check1 = len1 + len2 <= len3
    check2 = len2 + len3 <= len1
    check3 = len3 + len1 <= len2
    if (check1 or check2 or check3):
        print("Triangle NOT possible")
    else:
        print("Triangle possible")
        
#7. Write a function evensFromList(lofInts)which takes a list and prints out the even numbers.
def evensFromList(lofInts):
    for num in lofInts:
        if num%2 ==0:
            print(num)
        
#8. negNonNeg(nums) takes a list of nums, puts out a list of all the [negati]ve numbers,
## and a list of all the numbers that are >= 0. Use two accumulator lists and append using l.append(x)
def negNonNeg(nums):
    neg = []
    nonNeg = []
    for num in nums:
        if num < 0:
            neg.append(num)
        else:
            nonNeg.append(num)
    print('Negative Values:', neg)
    print('Non-Negative Values:', nonNeg)
        
#9. A random walk describes a turtle repeatedly moving the same step size but turning in a random
#direction before each step. Use the turtle module and the random module to make the turtle execute 
#a random walk using a length of ten for each step.  The turtle will stop the first time it gets 200 steps 
#or greater from its start.  Generate a record of the turtle moving on the canvas and print out in the 
#shell the number of turtle moves taken before it stops.  Run your program 3 times.

import turtle
import random
wn = turtle.Screen()
alice = turtle.Turtle()

def randomWalkInBounds():
    startx, starty = alice.position() #get start position
    moves = 0 #moves counter
    dist = 0 #initialize distance from start
    while dist < 190: #go no more than 190 from start, so can't go out of bounds.
        turn = random.randrange(-360, 360)
        alice.lt(turn)
        alice.fd(10)
        moves += 1
        endx, endy = alice.position() #get new position
        dist = distBtwPts(startx, starty, endx, endy) #update distance from start
    print('Times moved:', moves)

    ##Run One: moved 89 times
    ##Run Two: moved 172 times
    ##Run Three: moved 312 times


#10. Zelle 3.16: Fibonacci sequence

def fibonacci():
    n = eval(input("What do you want to use as n?: "))
    prev = 0     ##Create three counters to keep track of current and previous numbers. 
    current = 1
    fib = 0
    for i in range(n-1):
        fib = current+prev #new fib is the sum of the currently remembered fib and its predecessor
        prev = current  #what had been 'current' fib becomes the 'previous' for next loop.
        current = fib  #the new fib becomes the 'current' fib for next loop.
    print("the nth fibonacci number is:", fib)


#11. Zelle 3.17: Newton's square root method.
##Math has already been imported above.
    
def newton():
    x = eval(input("number to find sqrt of:"))
    n = eval(input("number of times to guess:"))
    guess = x/2

    for i in range(n):             #Guess n times
        guess = (guess + x/guess)/2  #Apply Newton's method to update guess using its old value, using parens to maintain order of operations.

    diff = math.sqrt(x) - guess #once out of loop, find difference from sqrt(x)
    print("Final Guess:", guess)  #and report findings to user. 
    print("Difference from sqrt(x):", diff)

        
        
        
        
