Task_One_File = open("Numbers.txt","w") 


Number_One = int(input("Please input your first number "))
Number_Two = int(input("Please input a second number "))
Number_Three = int(input("Please input a third number "))
Number_four = int(input("Please input a forth number "))


Task_One_File.write(str(Number_One))
Task_One_File.write(str("\n"))
Task_One_File.write(str(Number_Two))
Task_One_File.write(str("\n"))
Task_One_File.write(str(Number_Three))
Task_One_File.write(str("\n"))
Task_One_File.write(str(Number_four))
Task_One_File.write(str("\n"))
Task_One_File.close()
