print("Please select two numbers to enter into an equation")
Number_One = int(input("Number one? "))
Number_Two = int(input("Number Two? "))
print("Now please select what you would like to do with these numbers")
print("Type 'A' if you would like to add these numbers")
print("Type 'B' if you would like to subtract these numbers")
print("Type 'C' if you would like to multiply these numbers")
print("Type 'D' if you would like to divide these numbers")
print("Type 'E' if you would like to square these numbers")
selection_Input = input("Enter letter for function")
if selection_Input == "A":
    print(Number_One+Number_Two)
elif selection_Input=="B":
    print(Number_One-Number_Two)
elif selection_Input=="C":
    print(Number_One/Number_Two)
elif selection_Input=="D":
    print(Number_One*Number_Two)
elif selection_Input=="E":
    print(Number_One**Number_Two)