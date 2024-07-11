import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Amit', 'Riya', 'Vikram', 'Sneha', 'Rahul'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Data Inspection
print("\nFirst few rows:")
print(df.head())

print("\nLast few rows:")
print(df.tail())

print("\nInfo:")
print(df.info())

print("\nDescriptive statistics:")
print(df.describe())

print("\nShape of DataFrame:", df.shape)
print("\nColumn names:", df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values in each column:")
print(df.isnull().sum())

# Data Exploration
print("\nSelecting 'Name' column:")
print(df['Name'])

print("\nFiltering rows where Age > 25:")
print(df[df['Age'] > 25])

print("\nSorting by Age:")
print(df.sort_values(by='Age'))

df['Score'] = [85, 90, 78, 88, 95]
print("\nDataFrame after adding 'Score' column:")
print(df)

print("\nAverage age by city:")
print(df.groupby('City')['Age'].mean())

# Handling Missing Data
# Adding a column with missing values
df['Height'] = [5.5, 6.1, None, 5.9, 5.7]
print("\nDataFrame with missing values:")
print(df)

# Filling missing values
df['Height'].fillna(df['Height'].mean(), inplace=True)
print("\nDataFrame after filling missing values in 'Height' column:")
print(df)

# Dropping rows with any missing values
df.dropna(inplace=True)
print("\nDataFrame after dropping rows with any missing values:")
print(df)
