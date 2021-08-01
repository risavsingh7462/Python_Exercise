'''
Author: Sanjiv Paul
Date: 25 Jully 2021
Title: Guess_the_number
Story: So we made a program in which the user has to guess a number. We take input from the user a number and that number is smaller than our number, then our program will say to enter a number slightly larger than this, and if the user's number is greater than our number, then our program will say, enter a number slightly smaller than this, and the user will just guess the number only 9 times if you do more than that the game will be over. 
Note: This programe will have more interesting when i am useing random module on this.

'''
# import random
# actualNumber=random.randint(10, 100)

actualNumber=18

# initializing number_of_guesses
number_of_guesses=1

print("Number of guesses is limited to only 9 times:")
# starting a while loop
while(number_of_guesses<=9):
    user_guess_number=int(input("Guess the number:\n"))

# if else statement
    # if user_guess_number<actualNumber:
    if user_guess_number<18:
        print("You have enter less number please input greater number:\n")

    # elif user_guess_number>actualNumber:
    elif user_guess_number>18:
        print("You have enter greater number please input less number:\n")

    else:
        print("You won!:")
        print(number_of_guesses, "number of guesses you took to finished\n")

        break

    # count number of guesses
    print(9-number_of_guesses, "number of guesses left")

    number_of_guesses=number_of_guesses+1
    if(number_of_guesses>9):
        print("GAME OVER!!$")

    # THANK YOU