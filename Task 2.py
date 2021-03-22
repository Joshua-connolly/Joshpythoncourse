Ask_Joke = int(input("Want to hear a joke? Pick a number between 1 and 100 for a random chuckle"))

if Ask_Joke in range(1,26):
    print("Knock Knock")
elif Ask_Joke in range(26,51):
    print("A man walks into a bar")
elif Ask_Joke in range(51-69):
    print("How many developers does it take to write a funny joke")
elif Ask_Joke == 69: 
    print("There's always one isn't there... :P")
else: 
    print("why did the chicken cross the road")