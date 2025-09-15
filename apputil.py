
import pandas as pd


# update/add code below ...
# EXERCISE 1
def fib(n):
    """
    Recursive function to calculate the nth Fibonacci number
    Fibonacci series is F(0)=0, F(1)=1,F(n)=(n-1)+(n-2) for n>1
    """
    # Base case 1:
    if n == 0:
     return 0
    # Base case 2:
    elif n == 1 :
     return 1
    # Recursive case: sum of two previous Fibonacci numbers
    else:
     return fib(n-1) + fib(n-2)

    #print first 10 fibonacci numbers

#for i in range(10):
    #print(fib(i), end=" ")

    #EXERCISE 2:

def factorial(n):
    """
    Recursive function to calculate factorial of n.
    0! = 1, n! = n*(n-1)! for n>0
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def to_binary(n):
      """ Recursive function to convert a decimal number n to its binary representation 
      Args:
        n (int): The decimal number to be converted.
      """
      # Base case 1:
      if n == 0:
       return "0"
      # Base case 2:
      elif n == 1:
        return "1"
      else:
      # Recursive case: divide n by 2 and concatenate the remainder
       return to_binary(n // 2) + str(n % 2)
       
        #print binary representation of 10
#print (to_binary(10))

# print binary representation of 10 using built-in function
#print(bin(10)[2:])

   #EXERCISE 3:

url ='https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df = pd.read_csv(url)

#Part 1: Count missing values in each column
""" 
To get the number of missing values in each column, we can use the isnull() method to create a boolean DataFrame indicating where values are missing, and then use the sum() method to count the number of True values (i.e., missing values) in each column. 
 returns a Series with the count of missing values for each column.    
"""
#Count missing values in each column
missing_values = df.isnull().sum()
#print(missing_values)

#Sort columns by number of missing values
sorted_missing_values = missing_values.sort_values(ascending=True)
#print(sorted_missing_values)

#Get list of columns sorted by number of missing values
sorted_columns = sorted_missing_values.index.tolist()

#print list of columns sorted by number of missing values
#print(sorted_columns)

#part 2: Return dataframe with two columns
"""
Return a dataframe with two columns 'year' and 'total_admissions' showing the total number of admissions per year
"""

# 'year' and 'total_admissions' showing the total number of admissions per year
# Group by 'year_admitted' and count the number of admissions per year
df['date_in'] = pd.to_datetime(df['date_in'], errors='coerce')

admissions_per_year = (
  # group by year using dt.year to extract year from datetime
    df.groupby(df['date_in'].dt.year)  
    # Extract year from 'date_in' column   
      .size()
      #reset index to turn the Series into a DataFrame with 'year' and 'Total_admissions' columns
      .reset_index(name="total_admissions")
      .rename(columns={"date_in": "year"})
)
#print(admissions_per_year)

#part 3:Return a series
"""
Return a series with the average age
"""
# showing the average age 
avg_age_by_gender = df.groupby('gender')['age'].mean()
# print the average
#print(avg_age_by_gender)

#part 4:Return 5 common professions in order of prevalence
"""
Return a series with the 5 most common professions in order of prevalence
"""

# Count the occurrences of each profession
common_professions = df['profession'].value_counts()

