
import pandas as pd 
Destinations = pd.read_csv("Destinations.csv")
print(Destinations.shape)

print(Destinations.iloc[3:9])

print(Destinations["Number of all inclusive hotels "].mean())

Low_Dest = Destinations.nsmallest(1,"Feedback Score ",keep='first')
High_Dest = Destinations.nlargest(1,"Feedback Score ",keep='first')
print(Low_Dest)
print(High_Dest)

Filter = Destinations["Number of all inclusive hotels "] > 9

print(Destinations[Filter])

Filter_2 = Destinations["Feedback Score "] > 8

print(Destinations[Filter_2])

Filter_3 = Destinations["Feedback Score "] < 2

print(Destinations[Filter_3]) #Hotel Star Rating is 5 across the board which is highest so keep it in. 

print(Destinations.plot())

print(Destinations.plot.scatter(x='Number of all inclusive hotels ' ,y='Feedback Score ')) #No Corrolation 
print(Destinations.plot.scatter(x='Destinations ' ,y='Feedback Score ')