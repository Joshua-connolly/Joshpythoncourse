Welcome_Message = "Good afternoon Sir/Madam, welcome to the data diner!"
print(Welcome_Message)

def Meal_Order():
    Starter_Input = str(input("What can we get you for starters?"))

    print("Great choice! "+ Starter_Input + " Is one of our classic dishes.")

    Main_Input = str(input("Now what about for main? "))

    Dessert_Input = str((input("Lovely, and dessert? ")))

    Confirmation_Input = str(input("Right so, so far we have " + Starter_Input + ", " + Main_Input + ", " + Dessert_Input +" Is that correct?"))

    while Confirmation_Input not in {"yes", "no"}:
        print("please enter 'yes' or 'no'")
        Confirmation_Input = str(input("Right so, so far we have " + Starter_Input + ", " + Main_Input + ", " + Dessert_Input +" Is that correct?"))
    if Confirmation_Input == "yes":
        Drink_Input = str(input("Perfect, now what can i get you to drink with that, my recommendation is Fanta lemon?"))
        print("okay then, so that completes the order, we have " + Starter_Input + " for starters, " + Main_Input + "for main, " + Dessert_Input + "for dessert. With " +Drink_Input +"I will get that right for you.")
    else: Meal_Order()
Meal_Order()

