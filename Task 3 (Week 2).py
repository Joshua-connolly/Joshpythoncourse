def Calculator_Procedure(Inp_Number_1,Inp_Number_2,Inp_Operator):
     Number_1=Inp_Number_1   
     Number_2=Inp_Number_2   
     Operator=Inp_Operator     

     if Operator == "+":
        print(Number_1 + Number_2)
     elif Operator == "-":
        print(Number_1-Number_2)
     elif Operator == "/":
        print(Number_1/Number_2 )
     elif Operator == "*":
        print(Number_1*Number_2)

     Continue = input("Would you like to perform another calculation? (Y/N) ")
     if Continue == "Y":
        Inputs_()
     else :
        quit()  
        
def Inputs_(): 
     Number_1=int(input("Please input your first number "))  
     Number_2=int(input("Please input your second number ")) 

     Operator = input("Please type one of the following operators you would like to a apply to your numbers, +,-,/,* ") 
        
        
     Calculator_Procedure(Number_1,Number_2,Operator)


Inputs_()

