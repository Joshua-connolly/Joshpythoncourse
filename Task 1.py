import random
random_Number = random.randint(1,3)

user_Name = input("What is your name?")

print("Hi" + user_Name + ", I am thinking of a number between 1 and 10. Can you guess what that number is?")
print("What number am i thinking of?")

Guess_Input = int(input())

while Guess_Input != random_Number:
    print("uh oh, try again, " + user_Name)
    print("What number am i thinking of?")
    Guess_Input = int(input())

print("Yes, thats correct " + user_Name)