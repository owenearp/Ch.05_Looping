import random

'''
 1. Make the following program work.
   '''
# print("This program takes three numbers and returns the sum.")
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# num3 = int(input("Enter a number: "))
# total = num1 + num2 + num3
# print("Your total is:",total)


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(2,101,2):
#     print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# blasted = False
# while not blasted:
#     for i in range(10,-1,-1):
#         print(i)
#     blasted = True
#     print("Blast off!")



'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# num = random.randrange(1,11)
# print(num)





'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
pos = 0
neg = 0
zero = 0
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))
num6 = int(input("Enter a number: "))
num7 = int(input("Enter a number: "))
total = num1 + num2 + num3 + num4 + num5 + num6 +num7
print("The total of these numbers is",total)
if num1>0:
    pos += 1
elif num1<0:
    neg += 1
else:
    zero += 1
if num2>0:
    pos += 1
elif num2<0:
    neg += 1
else:
    zero += 1
if num3>0:
    pos += 1
elif num3<0:
    neg += 1
else:
    zero += 1
if num4>0:
    pos += 1
elif num4<0:
    neg += 1
else:
    zero += 1
if num5>0:
    pos += 1
elif num5<0:
    neg += 1
else:
    zero += 1
if num6>0:
    pos += 1
elif num6<0:
    neg += 1
else:
    zero += 1
if num7>0:
    pos += 1
elif num7<0:
    neg += 1
else:
    zero += 1
print("There are",pos,"positive numbers.")
print("There are",neg,"negative numbers.")
print(zero,"of the numbers are zero.")