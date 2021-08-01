'''
Author: Sanjiv paul
Date: 22 jully 2021
Purpose: Make faulty calculator

Story: The story is that you are a teacher and you want to take math test of the children of your class and you will not allow them to cheat, then you will give them a calculator, a calculator in which maths questions have been asked if the students calculate them. The wrong answer will come due to which they will not be able to cheat but the calculator will calculate everything else correctly.
And those numbers are 56*9=456, 78/23=20 ,986-45=888
'''
# solution

# take inputs from user 
user_firstInput = int(input("Enter your first number:\n"))
user_secondInput = int(input("Enter your second number:\n"))
user_oppInput = input("Enter your operator: +, -, *, /\n")

#faulty calculations 
if user_firstInput==56 and user_secondInput==9 and user_oppInput=='*':
    print("Your answer is: 456")
elif user_firstInput==78 and user_secondInput==23 and user_oppInput=='/':
    print("Your answer is: 20")
elif user_firstInput== 986 and user_secondInput==45 and user_oppInput=='-':
    print("Your answer is: 931")

# there calculate correct answers
elif user_oppInput=='+':
    print("Your answer is:", user_firstInput + user_secondInput)
elif user_oppInput=='-':
    print("Your answer is:", user_firstInput - user_secondInput)
elif user_oppInput=='*':
    print("Your answer is:", user_firstInput * user_secondInput)
elif user_oppInput=='/':
    print("Your answer is:", user_firstInput / user_secondInput)
else:
    print("Invalid input!")
print("Thank You For Using This Calculator")