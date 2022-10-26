import random
'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits print an end game message and their win/loss/tie record

'''
import math
done = False
tie = 0
win = 0
lose = 0
while not done:
    player = int(input("Enter your move here: "))
    ai = random.randint(1,3)
    if player==1 and ai==1:
        print("It's a tie! Both you and the computer chose Rock!")
        tie += 1
    elif player==2 and ai==2:
        print("It's a tie! Both you and the computer chose Paper!")
        tie += 1
    elif player==3 and ai==3:
        print("It's a tie! Both you and the computer chose Scissors!")
        tie += 1
    elif player==1 and ai==2:
        print("You lost! The computer chose Paper and you chose Rock!")
        lose += 1
    elif player==1 and ai==3:
        print("You won! The computer chose Scissors and you chose Rock!")
        win += 1
    elif player==2 and ai==1:
        print("You won! The computer chose Rock and you chose Paper!")
        win += 1
    elif player==2 and ai==3:
        print("You lost! The computer chose Scissors and you chose Paper!")
        lose += 1
    elif player==3 and ai==1:
        print("You lost! The computer chose Rock and you chose Scissors!")
        lose += 1
    elif player==3 and ai==2:
        print("You won! The computer chose Paper and you chose Scissors!")
        win += 1
    if player==4:
        score = input("Before you quit, do you want to see your score? ")
        if score.lower()=="yes" or score.lower()=="y":
            print("You won",win,"games, lost",lose,"games, and tied",tie,"games.")
            done = True
        else:
            done = True





