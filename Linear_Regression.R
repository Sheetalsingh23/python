# TECOA166 
#Sheetal Singh

# Include Salary Dataset
data <- read.csv("Salary_Data.csv")
print(data)

# Apply the lm() function.
x <- data$YearsExperience
y <- data$Salary
relation <- lm(y ~ x)
print(relation)
print(summary(relation))


# Find Salary of a person with Experience of 4 years.
a <- data.frame(x = 4)
result <- predict(relation,a)
print(result)
