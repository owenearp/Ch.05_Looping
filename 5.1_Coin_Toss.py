import random
'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
result = 0
totalHeads = 0
totalTails = 0
for i in range(50):
    result = random.randint(0, 1)
    if result==0:
        print("Heads!")
        totalHeads += 1
    else:
        print("Tails!")
        totalTails += 1
print("The coin landed on Heads",totalHeads,"times.")
print("The coin landed on Tails",totalTails,"times.")














