import random
'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''
import random
done = False
drinks = 5
miles = 0
thirst = 0
nativeMiles = -20
tired = 0
winner = False
dead = False
moved = False
print("Welcome to Journey across the Sahara!")
print()
print("While traveling across the desert, you accidentally disturbed an ancient native burial ground.")
print("The natives are now chasing you, and you need to get out of the desert as soon as possible.")
print("To survive, you will need to keep you and your camel in good health, while still maintaining a steady pace.")
print("The end of the desert is 200 miles away, so good luck!")
while not done:
    oasis = random.randint(1, 30)
    sandstorm = random.randint(1,40)
    severeSandstorm = random.randint(1,70)
    rain = random.randint(1,100)
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    print("Choose an action!")
    print()
    print("A: Drink from your canteen")
    print("B: Ahead at a moderate pace")
    print("C: Ahead at full speed")
    print("D: Stop for the night")
    print("E: Status check")
    print("Q: Quit game")
    print()
    choice = input("Action: ")
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print()
    if choice.lower()=="q":
        done = True
    elif choice.lower()=="a":
        if drinks == 0:
            print("You have no water left.")
        else:
            thirst = 0
            drinks -= 1
            if done == False:
                print("You chose to take a drink from your canteen.")
        moved = False
    elif choice.lower()=="b":
        distance = random.randint(5,12)
        miles += distance
        distance = 0
        nativeDistance = random.randint(7,14)
        nativeMiles += nativeDistance
        nativeDistance = 0
        thirst += 1
        tired += 1
        moved = True
        if done == False:
            print("You chose to go ahead at a moderate pace.")
    elif choice.lower()=="c":
        distance = random.randint(10,20)
        miles += distance
        distance = 0
        nativeDistance = random.randint(7,14)
        nativeMiles += nativeDistance
        nativeDistance = 0
        thirst += 1
        tired += random.randint(1,3)
        moved = True
        if done == False:
            print("You chose to go ahead full speed.")
    elif choice.lower()=="d":
        tired = 0
        nativeDistance = random.randint(7,14)
        nativeMiles += nativeDistance
        nativeDistance = 0
        if done == False:
            print("You chose to stop for the night and rest.")
        moved = False
    elif choice.lower()=="e":
        print("Miles traveled:",miles)
        print()
        print("Drinks in canteen:",drinks)
        print()
        print("The natives are",miles - nativeMiles,"miles behind you.")
        moved = False
    else:
        print("Please choose one of the provided choices.")

    if thirst == 4 and done == False:
        print()
        print("You are thirsty!")
    elif thirst == 5 and done == False:
        print()
        print("You are very thirsty!")
    elif thirst >= 6 and done == False:
        print()
        print("You have died of thirst.")
        print()
        print("Game Over!")
        print()
        print("-------------------------------------------------------------------------------------------------------")
        done = True
        dead = True
    if tired== 5 and done == False:
        print()
        print("Your camel is getting tired!")
    elif tired == 6 and done == False:
        print()
        print("Your camel is tired!")
    elif tired == 7 and done == False:
        print()
        print("Your camel is very tired!")
    elif tired >= 8 and done == False:
        print()
        print("Your camel has died, leaving you to die in the middle of the desert.")
        print()
        print("Game Over!")
        print()
        print("-------------------------------------------------------------------------------------------------------")
        done = True
        dead = True
    if nativeMiles >= miles and done == False:
        print()
        print("The natives have caught up to you and killed you.")
        print()
        print("Game Over!")
        print()
        print("-------------------------------------------------------------------------------------------------------")
        done = True
        dead = True
    elif miles - nativeMiles <= 15:
        print()
        print("The natives are getting close!")
    if miles >= 200 and done == False:
        print()
        print("You have traversed 200 miles through the desert and escaped the natives!")
        print()
        print("Great Job!")
        print()
        print("-------------------------------------------------------------------------------------------------------")
        winner = True
        done = True
    if oasis == 1 and not dead and not winner and sandstorm != 1 and severeSandstorm != 1 and rain != 1 and moved==True:
        if choice.lower()=="b" or choice.lower()=="c":
            print()
            print("You have stumbled upon an oasis! Lucky! You have refilled your canteen and rested.")
            thirst = 0
            drinks = 5
            tired = 0
    if sandstorm == 1 and not dead and not winner and oasis != 1 and severeSandstorm != 1 and rain != 1 and moved==True:
        print()
        print("Uh oh, you got caught in a sandstorm! You and your camel are thirsty and tired!")
        drinks -= 1
        thirst += 2
        tired += 3
        if thirst >= 6 and done == False:
            print()
            print("You have died of thirst.")
            print()
            print("Game Over!")
            print()
            print("---------------------------------------------------------------------------------------------------")
            done = True
            dead = True
        if tired >= 8 and done == False:
            print()
            print("Your camel has died, leaving you to die in the middle of the desert.")
            print()
            print("Game Over!")
            print()
            print("-------------------------------------------------------------------------------------------------------")
            done = True
            dead = True
    if severeSandstorm == 1 and not dead and not winner and oasis != 1 and sandstorm != 1 and rain != 1 and moved==True:
        print()
        print("Uh oh, you got caught in a very severe sandstorm! You and your camel are thirsty and tired.")
        drinks -= 2
        thirst += 3
        tired += 5
        if thirst >= 6 and done == False:
            print()
            print("You have died of thirst.")
            print()
            print("Game Over!")
            print()
            print("---------------------------------------------------------------------------------------------------")
            done = True
            dead = True
        if tired >= 8 and done == False:
            print()
            print("Your camel has died, leaving you to die in the middle of the desert.")
            print()
            print("Game Over!")
            print()
            print("-------------------------------------------------------------------------------------------------------")
            done = True
            dead = True
    if rain == 1 and not dead and not winner and oasis != 1 and sandstorm != 1 and severeSandstorm != 1:
        print()
        print("Wow! It's raining! In the desert! That's pretty rare, you have refilled some of your canteen.")
        drinks += 3
