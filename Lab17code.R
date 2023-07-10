install.packages("dplyr")
install.packages("ggplot2")
install.packages("read_excel")

library(dplyr)  # For data manipulation
library(ggplot2)  # For data visualization
library(readxl)	# For reading excel files

#read the excel file from the path provided
data <- read_excel("C:/Users/ajayi/Downloads/modified.xlsx")
head(data) #prints the data

#group the data by company size and calculate the average salary for each group
salary_by_size <- data %>%
  group_by(company_size) %>%
  summarise(avg_low_salary = mean(low_salary, na.rm= TRUE),
            avg_medium_salary = mean(medium_salary, na.rm= TRUE),
            avg_high_salary = mean(high_salary, na.rm= TRUE))

#plot the company size against average of high salaries
#the plot represents the average high salary for each category of company size. 
plotHigh <- ggplot(salary_by_size, aes(x = company_size, y = avg_high_salary)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(x = "Company Size", y = "Average High Salary") +
  ggtitle("Relationship between Company Size and Average High Salary")
plotHigh

#plot the company size against average of medium salaries
#the plot represents the average medium salary for each category of company size.
plotMed <- ggplot(salary_by_size, aes(x = company_size, y = avg_medium_salary)) +
  geom_bar(stat = "identity", fill = "green") +
  labs(x = "Company Size", y = "Average Medium Salary") +
  ggtitle("Relationship between Company Size and Average Medium Salary")
plotMed

#plot the company size against average of low salaries
#the plot represents the average low salary for each category of company size.
plotLow <-ggplot(salary_by_size, aes(x = company_size, y = avg_low_salary)) +
  geom_bar(stat = "identity", fill = "purple") +
  labs(x = "Company Size", y = "Average Low Salary") +
  ggtitle("Relationship between Company Size and Average Low Salary")
plotLow

