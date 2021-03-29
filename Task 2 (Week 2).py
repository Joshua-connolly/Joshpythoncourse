def Sales_Reduction(Inp_item,Inp_Cost,Inp_discount):
    Item = Inp_item
    Cost = Inp_Cost
    Discount = Inp_discount

    print("The " + Item + " initially cost £" + str(Cost) + ". However, with a " + str(Discount) + "percent discount, it now costs " + str(int(Cost-((Cost/100)*Discount))))

    return


Item = input("What Item would you like to reduce ")
Cost = int(input("How much is this item "))
Discount = int(input("What discount would you like to apply (%) "))

Sales_Reduction(Item,Cost,Discount)

def Reduction_to(Inp_item,Inp_Cost,Inp_discount,Inp_DisTo):

    Item = Inp_item
    Cost = Inp_Cost
    Discount = Inp_discount
    Discount_To = Inp_DisTo

    while Cost > Discount_To:
        print(int(Cost))
        Cost-=((Cost/100)*Discount)
    return

Item = input("What Item would you like to review a reduction trend with? ")
Cost = int(input("How much is this item currently? "))
Discount = int(input("What discount trend would you like to apply (%) "))
Discount_To = int(input("What cost would you like to review this products discount to? "))

Reduction_to(Item,Cost,Discount,Discount_To)

