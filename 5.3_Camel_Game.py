import random
'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book
'''
class colours:
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    pink = '\033[95m'
    aqua = '\033[96m'
    white = '\033[97m'
    lightGray = '\033[98m'
    red = '\033[91m'
    gray = '\033[90m'
    black = '\033[30m'
    purple = '\033[35m'
import random
done = False
drinks = 8
miles = 0
thirst = 0
nativeMiles = -20
tired = 0
winner = False
dead = False
moved = False
contamination = False
boxPossible = True
rainPossible = True
sandstormPossible = True
severePossible = True
oasisPossible = True
print(colours.yellow+f'')
print("Welcome to Journey across the Desert!")
print(colours.pink+f'')
print("While traveling across the desert, you accidentally disturbed an ancient native burial ground.")
print("The natives are now chasing you, and you need to get out of the desert as soon as possible.")
print("To survive, you will need to keep you and your camel in good health, while still maintaining a steady pace.")
print("The end of the desert is 300 miles away.")
print("Make sure to play the game multiple times to see all the events that can occur.")
print("Make sure to read the game top to bottom.")
print("By using some common sense you should be able to beat the game in a few tries. Good luck!")
print(colours.red)
print("Made by: Owen Earp")
while not done:
    oasis = random.randint(1, 20)
    sandstorm = random.randint(1,40)
    severeSandstorm = random.randint(1,60)
    rain = random.randint(1,60)
    box = random.randint(1,50)
    boxPoisoned = random.randint(1,2)
    print(colours.white + f'')
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(colours.blue + f'')
    print("Choose an action!")
    print(colours.pink + f'')
    print("A: Drink from your water bottle")
    print("B: Ahead at a moderate pace")
    print("C: Ahead at full speed")
    print("D: Stop for the night")
    print("E: Status check")
    print("Q: Quit game")
    print(colours.blue + f'')
    choice = input("Action: ")
    print(colours.white + f'')
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if choice.lower()=="q":
        done = True
    elif choice.lower()=="a":
        if contamination == True:
            print(colours.yellow)
            print("Uh oh, turns out that liquid from earlier was not water. But it was very poisonous.")
            print(colours.red)
            print("You have been poisoned, resulting in your death.")
            print(colours.yellow)
            print("Game Over!")
            print(colours.white)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            done = True
            dead = True
        if drinks == 0:
            print(colours.red + f'')
            print("You have no water left.")
        elif drinks == 5 and not done:
            print(colours.aqua + f'')
            print("You took a drink from your water bottle.")
            print(colours.green)
            print("By looking in your bottle, you can tell that you have drunk about half of your water.")
            thirst = 0
            drinks -= 1
        elif not done:
            print(colours.aqua + f'')
            print("You decided to take a drink from your water bottle.")
            print(colours.green)
            print("You are no longer thirsty.")
            thirst = 0
            drinks -= 1
        moved = False
    elif choice.lower()=="b":
        distance = random.randint(5,12)
        miles += distance
        nativeDistance = random.randint(7,14)
        nativeMiles += nativeDistance
        nativeDistance = 0
        thirst += 1
        tired += 1
        moved = True
        if done == False:
            print(colours.aqua + f'')
            print("You decided to travel ahead at a moderate pace.")
            print(colours.green + f'')
            print("You traveled",distance,"miles.")
            distance = 0
    elif choice.lower()=="c":
        distance = random.randint(10,20)
        miles += distance
        nativeDistance = random.randint(7,14)
        nativeMiles += nativeDistance
        nativeDistance = 0
        thirst += 1
        tired += random.randint(1,3)
        moved = True
        if done == False:
            print(colours.aqua + f'')
            print("You decided to travel ahead at full speed.")
            print(colours.green + f'')
            print("You traveled",distance,"miles.")
            distance = 0
    elif choice.lower()=="d":
        tired = 0
        nativeDistance = random.randint(7,14)
        nativeMiles += nativeDistance
        nativeDistance = 0
        if done == False:
            print(colours.aqua + f'')
            print("You decided to stop for the night and rest.")
            print(colours.green + f'')
            print("Your camel is no longer tired.")
        moved = False
    elif choice.lower()=="e":
        print(colours.blue + f'')
        print("Your Status:")
        print(colours.purple + f'')
        print("Miles traveled:", colours.aqua, miles)
        print(colours.purple)
        print("Drinks in water bottle:", colours.aqua, drinks)
        print(colours.purple)
        print("Distance away from natives:", colours.aqua, miles - nativeMiles)
        moved = False
    else:
        print(colours.red)
        print("Please choose one of the provided choices.")
    if thirst == 4 and done == False:
        print(colours.yellow)
        print("You are thirsty!")
    elif thirst == 5 and done == False:
        print(colours.red)
        print("You are very thirsty!")
    elif thirst >= 6 and done == False:
        print(colours.red)
        print("You have died of thirst.")
        print(colours.yellow)
        print("Game Over!")
        print(colours.white)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        done = True
        dead = True
    if tired== 5 and done == False:
        print(colours.yellow)
        print("Your camel is getting tired!")
    elif tired == 6 and done == False:
        print(colours.yellow)
        print("Your camel is tired!")
    elif tired == 7 and done == False:
        print(colours.red)
        print("Your camel is very tired!")
    elif tired >= 8 and done == False:
        print(colours.red)
        print("Your camel has died, leaving you in the middle of the desert to die.")
        print(colours.yellow)
        print("Game Over!")
        print(colours.white)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        done = True
        dead = True
    if nativeMiles >= miles and done == False:
        print(colours.red)
        print("The natives have caught up to you and killed you.")
        print(colours.yellow)
        print("Game Over!")
        print(colours.white)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        done = True
        dead = True
    elif miles - nativeMiles <= 15:
        print(colours.yellow)
        print("The natives are getting close!")
    if miles >= 300 and done == False:
        print(colours.aqua)
        print("You have traversed 300 miles through the desert and escaped the natives!")
        print(colours.green)
        print("Great Job!")
        print(colours.white)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        winner = True
        done = True
    if oasis == 1 and not dead and not winner and sandstorm != 1 and severeSandstorm != 1 and rain != 1 and moved==True and oasisPossible == True:
        oasisPossible = True
        if choice.lower()=="b" or choice.lower()=="c":
            print(colours.aqua)
            print("You have stumbled upon an oasis!")
            print(colours.green)
            print("You have gained water and your camel is no longer tired.")
            thirst = 0
            drinks = 6
            tired = 0
    if sandstorm == 1 and not dead and not winner and oasis != 1 and severeSandstorm != 1 and rain != 1 and moved==True and box != 1 and sandstormPossible == True:
        sandstormPossible = True
        print(colours.yellow)
        print("Uh oh, you got caught in a sandstorm!")
        print(colours.red)
        print("It has impacted your thirst and your camel's tiredness.")
        thirst += 1
        tired += 2
        if thirst == 4 and done == False:
            print(colours.yellow)
            print("You are thirsty!")
        elif thirst == 5 and done == False:
            print(colours.red)
            print("You are very thirsty!")
        if tired == 5 and done == False:
            print(colours.yellow)
            print("Your camel is getting tired!")
        elif tired == 6 and done == False:
            print(colours.yellow)
            print("Your camel is tired!")
        elif tired == 7 and done == False:
            print(colours.red)
            print("Your camel is very tired!")
        if thirst >= 6 and done == False:
            print(colours.red)
            print("You have died of thirst.")
            print(colours.yellow)
            print("Game Over!")
            print(colours.white)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            done = True
            dead = True
        elif tired >= 8 and done == False:
            print(colours.red)
            print("Your camel has died, leaving you in the middle of the desert to die.")
            print(colours.yellow)
            print("Game Over!")
            print(colours.white)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            done = True
            dead = True
    if severeSandstorm == 1 and not dead and not winner and oasis != 1 and sandstorm != 1 and rain != 1 and moved==True and box != 1 and severePossible == True and miles >= 200:
        severePossible = True
        print(colours.yellow)
        print("Uh oh, you got caught in a very severe sandstorm!")
        print(colours.red)
        print("Your thirst and your camel's tiredness are badly affected.")
        drinks -= 1
        thirst += 2
        tired += 3
        if thirst == 4 and done == False:
            print(colours.yellow)
            print("You are thirsty!")
        elif thirst == 5 and done == False:
            print(colours.red)
            print("You are very thirsty!")
        if tired == 5 and done == False:
            print(colours.yellow)
            print("Your camel is getting tired!")
        elif tired == 6 and done == False:
            print(colours.yellow)
            print("Your camel is tired!")
        elif tired == 7 and done == False:
            print(colours.red)
            print("Your camel is very tired!")
        if thirst >= 6 and done == False:
            print(colours.red)
            print("You have died of thirst.")
            print(colours.yellow)
            print("Game Over!")
            print(colours.white)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            done = True
            dead = True
        elif tired >= 8 and done == False:
            print(colours.red)
            print("Your camel has died, leaving you in the middle of the desert to die.")
            print(colours.yellow)
            print("Game Over!")
            print(colours.white)
            print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
            done = True
            dead = True
    if rain == 1 and not dead and not winner and oasis != 1 and sandstorm != 1 and severeSandstorm != 1 and box != 1 and rainPossible == True and miles >= 100:
        rainPossible = True
        print(colours.aqua)
        print("Wow! It's raining! In the desert!")
        print(colours.green)
        print("You have gained some water.")
        drinks += 3
    if box == 1 and not dead and not winner and oasis != 1 and sandstorm != 1 and severeSandstorm != 1 and rain != 1 and boxPossible == True and miles >= 150:
        if choice.lower() == "b" or choice.lower() == "c":
            print(colours.aqua)
            print("It seems you have found a small wooden box in the sand! Do you want to open it?")
            print(colours.blue)
            boxChoice = input("Choice: ")
            if boxChoice.lower()=="yes" or boxChoice.lower()=="y":
                print(colours.aqua)
                print("You decide to open the box. There is a bottle with some liquid in it.")
                print()
                print("It looks like water, but you aren't sure. Add the liquid to your water bottle?")
                print(colours.blue)
                takeLiquid = input("Choice: ")
                if takeLiquid.lower()=="yes" or takeLiquid.lower()=="y":
                    print(colours.green)
                    print("You have added this liquid to your water supply.")
                    if boxPoisoned == 1:
                        contamination = True
                        drinks += 1
                    elif boxPoisoned == 2:
                        contamination = False
                        drinks += 2
                else:
                    print(colours.aqua)
                    print("Good choice. It could be harmful.")

            else:
                print(colours.aqua)
                print("Good choice. You never know what could be in there.")