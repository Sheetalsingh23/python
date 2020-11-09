# TECOA166 
#Sheetal Singh

ds_mean <- function(ds) {
  cat("\nMean:-\n")
  print(sapply(ds[,1:4], mean, na.rm = T)) # find mean deviation 
}

getmode <- function(v) { 
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v, uniqv)))]  # Function to calulate mode
}

ds_mode <- function(ds) {
  cat("\nMode:-\n")
  cat("Sepal.Length: ",getmode(ds$Sepal.Length),"\n")
  cat("Sepal.Width: ",getmode(ds$Sepal.Width),"\n")
  cat("Petal.Length: ",getmode(ds$Petal.Length),"\n")
  cat("Petal.Width: ",getmode(ds$Petal.Width),"\n")
}

ds_median <- function(ds) {
  cat("\nMedian:-\n")
  print(sapply(ds[,1:4], median, na.rm = T)) # find median deviation 
}

ds_standard_deviation <- function(ds) {
  cat("\nStandard deviation:-\n")
  print(sapply(dataset[,1:4],sd)) # find standard deviation 
}

ds_varaition <- function(ds) {
  cat("\nVariance:-\n")
  print(sapply(dataset[,1:4],var)) # find variance 
}

ds_skewness <- function(ds) {
  cat("\nSkewness:-\n")
  #install.packages ("moments")
  library (moments)
  print(sapply(ds[,1:4],skewness)) # find skewness 
}

ds_kurtosis <- function(ds) {
  cat("\nKurtosis:-\n")
  #install.packages ("moments")
  library (moments)
  print(sapply(ds[,1:4],kurtosis)) # find kurtosis
}

ds_histogram<- function(ds) {
  hist(iris$Sepal.Width, col="yellow", ylim = c(0,40))
  hist(iris$Sepal.Length, col="pink", ylim = c(0,40))
  hist(iris$Petal.Width, col="lightblue", ylim = c(0,40))
  hist(iris$Petal.Length, col="darkorchid", ylim = c(0,40))
}

ds_boxplot<- function(ds) {
  irisVer <- subset(ds, Species == "versicolor")
  irisSet <- subset(ds, Species == "setosa")
  irisVir <- subset(ds, Species == "virginica")
  par(mfrow=c(1,3),mar=c(6,3,2,1))
  boxplot(irisVer[,1:4], main="Versicolor, Rainbow Palette",ylim = c(0,8),las=2, col=rainbow(4))
  boxplot(irisSet[,1:4], main="Setosa, Heat color Palette",ylim = c(0,8),las=2, col=heat.colors(4))
  boxplot(irisVir[,1:4], main="Virginica, Topo colors Palette",ylim = c(0,8),las=2, col=topo.colors(4))
  
}

ds_scatterplot<- function(ds) {
  my_cols <- c("#00AFBB", "#E7B800", "#FC4E07")  
  pairs(ds[,1:4], pch = 19,  cex = 0.5,
        col = my_cols[iris$Species],
        lower.panel=NULL)
  #par(xpd = TRUE)
  #legend("topright", fill = unique(iris$Species), legend = c( levels(iris$Species)))
}


# Main Program Starts form here
dataset <- iris # load dataset
while (TRUE)
{
  # Display Menu
  cat("\n\nMenu:-
1. Find mean
2. Find mode
3. Find median
4. Find standard deviation
5. Find variance
6. Compute skewness
7. Compute kurtosis
8. Histogram
9. Boxplot
10. Scatter Plot
11.Exit\n\n")
  
  # Take input form user
  ch = as.integer(readline(prompt="Enter Your Choice: ")) 
  
  # Perform action specified by user
  switch(ch,ds_mean(dataset),ds_mode(dataset),
         ds_median(dataset), ds_standard_deviation(dataset),
         ds_varaition(dataset),ds_skewness(dataset),
         ds_kurtosis(dataset), ds_histogram(dataset),
         ds_boxplot(dataset),ds_scatterplot(dataset))
  
  if(ch==11){break}
}


