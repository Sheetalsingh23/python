# TECOA166
#Sheetal Singh

#install.packages('ggplot2')
library(ggplot2)

# Funcions for perticular action

scatter_plot_1 <- function(d) {
  print(ggplot(data = d) +
    geom_point(mapping = aes(x = displ, y = hwy, color = class)))
}

scatter_plot_2 <- function(d) {
  print(ggplot(data = d) +
    geom_point(mapping = aes(x = displ, y = hwy)) +
    facet_wrap(~ class, nrow = 2))
}

line_graph <- function(d) {
  print(ggplot(data = d) +
    geom_line(
      mapping = aes(x = displ, y = hwy, color = drv)))
}

curve_plot <- function(d) {
  print(ggplot(data = d) +
    geom_smooth(
      mapping = aes(x = displ, y = hwy, color = drv)))
}

bar_plot <- function(d) {
  print(ggplot(d, aes(class, fill = drv)) +
    geom_bar(position = "dodge"))
}

pie_chart <- function(d) {
  print(ggplot(d, aes(x = factor(1), fill = drv)) +
    geom_bar(width = 1) +
    coord_polar(theta = "y"))
}

box_plot <- function(d) {
  print(ggplot(data = d, mapping = aes(x = class, y = hwy)) +
    geom_boxplot(aes(fill=class)))
}

# Main Program Starts form here
data<-ggplot2::mpg  # Dataset for visualization
#?mpg    # to know about mpg dataset
while (TRUE)
{
  # Display Menu
  cat("\n\nMenu:-
1. Scatter Plot 1
2. Scatter Plot 2
3. Line Graph
4. Curve Plot
5. Bar Plot
6. Pie Chart
7. Box Plot
8. Exit\n\n")
  
  # Take input form user
  ch = as.integer(readline(prompt="Enter Your Choice: ")) 
  
  # Perform action specified by user
  switch(ch,
         scatter_plot_1(data),
         scatter_plot_2(data),
         line_graph(data),
         curve_plot(data),
         bar_plot(data),
         pie_chart(data),
         box_plot(data))
  
  if(ch==8){break}
}