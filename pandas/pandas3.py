import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Amit', 'Riya', 'Vikram', 'Sneha', 'Rahul'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai'],
    'Score': [85, 90, 78, 88, 95],
    'Height': [5.5, 6.1, None, 5.9, 5.7]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Indexing and Selection
print("\nSelecting 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])

print("\nSelecting rows 2 to 4:")
print(df.iloc[1:4])

# Data Manipulation and Transformation
print("\nAdding a new column 'Status':")
df['Status'] = ['Single', 'Married', 'Single', 'Married', 'Single']
print(df)

print("\nUpdating 'Height' for missing values:")
df['Height'].fillna(df['Height'].mean(), inplace=True)
print(df)

# Handling Null Values
print("\nHandling Null Values:")
print("Number of null values in each column:")
print(df.isnull().sum())

# Data Transformation
print("\nTransforming 'Age' to a categorical variable:")
bins = [0, 25, 30, 35]
labels = ['Young', 'Mid-age', 'Senior']
df['Age_Category'] = pd.cut(df['Age'], bins=bins, labels=labels)
print(df)

# Visualization using Seaborn
print("\nVisualizing Age distribution:")
sns.histplot(data=df, x='Age', bins=3, kde=True)
plt.title('Age Distribution')
plt.show()
