import pandas as pd

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Series from a list:")
print(series)

# Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30}
series_dict = pd.Series(data_dict)
print("\nSeries from a dictionary:")
print(series_dict)

# Creating a Series with a custom index
data_custom = [10, 20, 30]
index_custom = ['a', 'b', 'c']
series_custom = pd.Series(data_custom, index=index_custom)
print("\nSeries with a custom index:")
print(series_custom)

# Accessing elements by position
print("\nAccessing element by position (0):", series_custom[0])  

# Accessing elements by label
print("Accessing element by label ('a'):", series_custom['a'])  

# Arithmetic operations
series_arith = pd.Series([1, 2, 3, 4, 5])
print("\nArithmetic operations:")
print("Series + 5:\n", series_arith + 5)  
print("Series * 2:\n", series_arith * 2)  

# Element-wise operations
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
print("\nElement-wise addition:")
print(series1 + series2) 
# Descriptive statistics
series_stats = pd.Series([1, 2, 3, 4, 5])
print("\nDescriptive statistics:")
print("Mean:", series_stats.mean()) 
print("Sum:", series_stats.sum())    
print("Max:", series_stats.max())    
print("Min:", series_stats.min())   
