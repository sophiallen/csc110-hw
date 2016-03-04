

from random import randint

def draw():
    opts = {1:'rock', 2:'paper', 3:'scissors'}
    choice = randint(1,3)
    return opts[choice]


def winner(hum, comp):
    if hum == comp:
        return (0,0)
    elif hum == "rock":
        if comp == "paper":
            return (-1, 3)
        else:
            return (3, -1)
    elif hum == "paper":
        if comp == "scissors":
            return (-1, 3)
        else:
            return (3,-1)
    elif hum == "scissors":
        if comp == "paper":
            return (3, -1)
        else:
            return (-1, 3)

def play():
    cscore = 0
    hscore = 0
    while cscore < 10 and hscore < 10:
        hum = input("rock, paper, or scissors? : ")
        comp = draw()
        print("computer drew:",comp)
        h, c = winner(hum, comp)
        if h > c:
            print("you won this round!")
        elif h < c:
            print("the computer won this round")
        else:
            print("tie!")
        cscore += c
        hscore += h
        print("Score:", hscore, cscore)
    print("final score: human: {0} computer {1}".format(hscore, cscore))
    
