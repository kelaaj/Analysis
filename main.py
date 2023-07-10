"""
AUTHOR : GIFT AJAYI
DATE: JULY - 07 - 2023
ABOUT: The purpose of this code is to compute the percentiles of the salaries given to use and use the percentiles to classify them as low, high or medium income earners and we can use this information to visualize what to do with our data 
"""

#import numpy and panda for analysis which gives you access to mathematical functions and also allows you to manipulate your data
import numpy as np
import pandas as pd

# read the csv file 
data = pd.read_csv('ds_salaries.csv')
# calculate the 3 major percentiles of the salary and store them in salary_percentiles
salary_percentiles = np.percentile(data['salary_in_usd'], [25, 50, 75])

#print the percentiles
print(salary_percentiles)

#from the array of salary percentiles set the low, medium, high salaries accordingly to the 25th, 50th, and 75th percentile
low_salary_threshold = salary_percentiles[0]
medium_salary_threshold = salary_percentiles[1]
high_salary_threshold = salary_percentiles[2]

#create a new column that tells you which level or percentile a salary in usd falls in, they could fall in either (low, medium or high)
data['Salary Level'] = pd.cut(
  data['salary_in_usd'],
  bins=[
    float('-inf'), low_salary_threshold, medium_salary_threshold,
    float('inf')
  ],
  labels=['Low Salary', 'Medium Salary', 'High Salary'])

# Check the updated dataset with the new column
print(data)

#creating new columns for low_salary, medium_salary, and high_salary
# Create new columns based on salary ranges and place the salaries in USD in the right range
data['low_salary'] = data[
  data['salary_in_usd'] <= low_salary_threshold]['salary_in_usd']
data['medium_salary'] = data[(data['salary_in_usd'] > low_salary_threshold) & (
  data['salary_in_usd'] <= medium_salary_threshold)]['salary_in_usd']
data['high_salary'] = data[
  data['salary_in_usd'] > medium_salary_threshold]['salary_in_usd']

# Check the updated dataset with the new columns
print(data)

data.to_csv('modified.csv')
