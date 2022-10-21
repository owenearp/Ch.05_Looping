import random

# for i in range(3):
#     print("a")
# for j in range(3):
#     print("b")

# for i in range(3):
#     print (i)
#     for j in range(3):
#         print(j)
# print("Done")

# total = 0
# for i in range(1,101):
#     total += i
# print(total)
#
# a = 0
# for i in range(10):
#     a+=1
#     for j in range(10):
#         a+=1
# print(a)
#
# for i in range(10):
#     print(i)

# i = 1
# while i<=2**32:
#     print(i)
#     i*=2

# quit = "n"
# while quit.lower()=="n":
#     quit= input("Do you want to quit?")
# print("Goodbye!")

# done = False
# perserverance = 0
# while not done:
#     quit = input("Do you want to quit?")
#     if quit.lower()=="y":
#         done = True
#     else:
#         perserverance+=1
# print("Goodbye! Your perserverance level is",perserverance)

# num = random.randrange(1,101)
# again = False
# tries = 1
# while again==False:
#     status = False
#     while status == False:
#         answer = int(input("Guess a number between 1 and 100: "))
#         if answer == num:
#             print("You figured out the number in",tries,"tries!")
#             status = True
#             again = input("Do you want to play again? ")
#             if again.lower()=="yes":
#                 quit = False
#                 num = random.randrange(1, 101)
#             elif again.lower()=="no":
#                 print("Thanks for playing!")
#                 again = True
#         elif answer < num:
#             print("Higher!")
#             tries = tries + 1
#         elif answer > num:
#             print("Lower!")
#             tries = tries + 1
# for letter in "Death Star":
#     if letter == " ":
#         continue
#     print("Current letter:",letter)
var = 0
while var <= 10:
    var += 1
    if var%2 != 0:
        pass
    print("Current variable value:",var)

print("Goodbye")