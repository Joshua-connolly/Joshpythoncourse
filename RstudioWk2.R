A <- runif(n = 5, min = -50, max = 50)
B <- runif(n = 5, min = -50, max = 50)
C <- runif(n = 5, min = -50, max = 50)
x <- cbind(A,B,C)

plot(x)





employee <- c('Peter','Alan','Sam','Rob','Timmy')
age <-c(17,64,23,43,65)
gender <- c('M','M','F','M','M')
role <- c('Support','Manager','Admin','Manager','Front of house')
lengthofservice <- c(3,2,5,2,7)
employee_data <- data.frame(employee, age, gender, role,lengthofservice)
print(employee_data)



install.packages('ggplot2')

library(ggplot2)
one <- 1:20
two <- x^2

Graph_data <- data.frame(one,two)
print(Graph_data)
ggplot(data = Graph_data,mapping = aes(x=one, y=two))

Subject<- c('biology','math','english','art','IT')
Score <-c(17,64,23,43,65)
barchart_data = data.frame(Subject,Score)
ggplot(data = barchart_data,mapping = aes(x=Subject,y=Score))+geom_histogram()
qplot(barchart_data$score, geom="histogram") 
         