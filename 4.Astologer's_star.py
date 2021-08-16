'''
Author: Sanjiv Paul
Date: 16 Augest 2021
Title: Astologer's_star

'''
print("HOW MANY ROW'S YOU WANT TO PRINT:")
input_one=int(input())
print("Type 1 or 0")
input_two=int(input())
new=bool(input_two)

if new == True:
    for i in range(1, input_one+1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

elif new == False:
    for i in range(input_one, 0, -1):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

# sanjiv paul, thank you