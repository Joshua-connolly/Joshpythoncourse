def mark_grade(Grade,Compare_Grade_input):   

     if Grade <= 30:
        print("Your current grade is C")
     elif Grade <=70 : 
        print("Your current grade is B")
     else :
        print("Your current grade is an A")
    

     Continue = input("Would you like to compare this with your target grade (Y/N) ")
     if Continue == "Y":
         if Compare_Grade_input == "A" and Grade <=30:
             print("I recommend that you work harder this isn't good enough" ) 
         elif Compare_Grade_input == "A" and Grade <=70:
             print("Close but not close enough")
         elif Compare_Grade_input == "A" and Grade <=100:
                 print("Well done, you are on track!")
         elif Compare_Grade_input == "B" and Grade <=30:
              print("I recommend that you work harder this isn't good enough" ) 
         elif Compare_Grade_input == "B" and Grade <=70:
             print("Well done, you are on track!")
         elif Compare_Grade_input == "C" and Grade <=30:
             print("Well done, you are on track!" ) 
         else:    
                 print("Well done, you are doing better than expected")
     else :
         quit()  
     return 
        
def Inputs_(): 
     Grade =int(input("Please input your percentage grade "))          
     Compare_Grade_input =input("Please input your target grade ")    
     mark_grade(Grade,Compare_Grade_input)


Inputs_()
    

