
import pandas as pd

# EXERCISE 1
def fibonacci(n):
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
     return fibonacci(n-1) + fibonacci(n-2)

    #EXERCISE 2:

def to_binary(n):
      """ Recursive function to convert a decimal number n to its binary representation 
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
      

   #EXERCISE 3:

url ='https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df = pd.read_csv(url)

#Part 1: Count missing values in each column
""" 
To get the number of missing values in each column, we can use the isnull() method to create a boolean DataFrame indicating where values are missing, and then use the sum() method to count the number of True values (i.e., missing values) in each column. 
 returns a Series with the count of missing values for each column.    
"""

def task_i():
#Count missing values in each column
 missing_values = df.isnull().sum()
#print(missing_values)

#Sort columns by number of missing values
 sorted_missing_values = missing_values.sort_values(ascending=True)
#print(sorted_missing_values)

#Get list of columns sorted by number of missing values
 sorted_columns = sorted_missing_values.index.tolist()
 return sorted_columns
task_i()

#part 2: Return dataframe with two columns
"""
Return a dataframe with two columns 'year' and 'total_admissions' showing the total number of admissions per year
"""

# 'year' and 'total_admissions' showing the total number of admissions per year
# Group by 'year_admitted' and count the number of admissions per year

def task_i():

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
 return admissions_per_year
task_i()

#part 3:Return a series
"""
Return a series with the average age
"""
def task_i():
# Create a copy of the DataFrame to avoid modifying the original data
    data = df.copy()

    # Ensure age is numeric
    data['age'] = pd.to_numeric(data['age'], errors='coerce')

    # Keep only rows where gender is male or female (case-insensitive)
    data['gender'] = data['gender'].str.lower()
    data.loc[~data['gender'].isin(['male', 'female']), 'gender'] = np.nan

    # Average age by gender (NaNs in gender are automatically excluded)
    return data.groupby('gender')['age'].mean()
task_i()


#part 4:Return 5 common professions in order of prevalence
"""
Return a series with the 5 most common professions in order of prevalence
"""
def task_i():

# Count the occurrences of each profession
 common_professions = df['profession'].value_counts()
# Get the top 5 most common professions
 top5_professions = df['profession'].value_counts().head(5)
 
 return top5_professions
task_i()

