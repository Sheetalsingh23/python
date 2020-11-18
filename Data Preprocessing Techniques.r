# TECOA166 
#Sheetal Singh
  
# Funcions for particular action

replace_na <- function(data) {
  cat("\nBefore Replace:-\n")
  print(data)
  
  data[is.na(data[,2]),2] <- round(mean(data$Age,na.rm = TRUE))
  data[is.na(data[,3]),3] <- round(mean(data$Salary,na.rm = TRUE))
  
  cat("\nAfter Replace:-\n")
  print(data)
}

delete_na <- function(data) {
  cat("\nBefore Delete:-\n")
  print(data)
  
  newdata<-na.omit(data)
  
  cat("\nAfter Delete:-\n")
  print(newdata)
}

age_outlier <- function(data) {
  #install.packages("outliers")
  library(outliers)
  find_age_outlier<- which(outlier(data$Age, logical=TRUE))
  cat("\nRow with Age Outlier:-\n")
  print(data[find_age_outlier,])
}

salary_outlier <- function(data) {
  #install.packages("outliers")
  library(outliers)
  find_salary_outlier<- which(outlier(data$Salary, logical=TRUE))
  cat("\nRow with Salary Outlier:-\n")
  print(data[find_salary_outlier,])
}

delete_outliers <- function(data) {
  cat("\nBefore Delete:-\n")
  print(data)
  
  #install.packages("outliers")
  library(outliers)
  find_age_outlier<- which(outlier(data$Age, logical=TRUE))
  newdata<-data[-find_age_outlier,]
  
  find_salary_outlier<- which(outlier(newdata$Salary, logical=TRUE))
  newdata<-newdata[-find_salary_outlier,]
  
  cat("\nAfter Delete:-\n")
  print(newdata)
}

encoding_categorical <- function(data) {
  cat("\nBefore Encoding:-\n")
  print(data)
  
  data$Country <- factor(data$Country , levels=c('France','Spain','Germany'),labels=c(1,2,3))
  data$Purchased <- factor(data$Purchased , levels=c('Yes','No'),labels=c(1,0))
  
  cat("\nAfter Encoding:-\n")
  print(data)
}

feature_scaling <- function(data) {
  data[is.na(data[,2]),2] <- round(mean(data$Age,na.rm = TRUE)) # replace NA before Feature Scaling
  data[is.na(data[,3]),3] <- round(mean(data$Salary,na.rm = TRUE))
  
  cat("\nBefore Feature Scaling:-\n")
  print(data[,2:3])
  
  newdata = scale(data[,2:3])
  
  cat("\nAfter Feature Scaling:-\n")
  print(newdata)
}

# Main Program Starts form here
data <- read.csv("Data.csv", header=TRUE, fileEncoding = "UTF-8-BOM") # load dataset
while (TRUE)
{
  # Display Menu
  cat("\n\nMenu:-
1. Replace missing/NULL values with mean
2. Delete rows with missing/NULL values
3. Show Age Outlier
4. Show Salary Outlier
5. Delete rows with outliers
6. Encoding of categorical data
7. Feature scaling
8. Exit\n\n")
  
  # Take input form user
  ch = as.integer(readline(prompt="Enter Your Choice: ")) 
  
  # Perform action specified by user
  switch(ch,
         replace_na(data),
         delete_na(data),
         age_outlier(data),
         salary_outlier(data),
         delete_outliers(data),
         encoding_categorical(data),
         feature_scaling(data))
  
  if(ch==8){break}
}