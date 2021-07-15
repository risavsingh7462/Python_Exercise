
'''
Author: Sanjiv Paul
Date: 15 Jully 2021
Excercise_name: A_Dictionary
'''
#Here we have created a dictionary which we named d2
#here back slas is a newline character
d2 = {"python":"Python is an interpreted high-level general-purpose programming language",
      "dictionary":"a book or electronic resource that lists the words of a language \n"
                   "(typically in alphabetical order) and gives their meaning, or gives\n "
                   "the equivalent words in a different language, often also providing information\n"
                   " about pronunciation, origin, and usage\n"}

print("Enter the word:\n")
#Here we took input from user
search=input()
# print("The required meaning is:")
# Here whatever input the user gives, it will search in D2
print(d2[search])
print("\nThank you for using me")