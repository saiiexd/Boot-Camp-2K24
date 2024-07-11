import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the 'tips' dataset
tips = sns.load_dataset('tips')

# Line Plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=tips, x='total_bill', y='tip', hue='day', style='day', markers=True, dashes=False)
plt.title('Line Plot of Tips by Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.grid(True)
plt.show()

# Histogram and KDE Plot
plt.figure(figsize=(10, 6))
sns.histplot(data=tips, x='total_bill', kde=True, bins=30, color='blue')
plt.title('Histogram and KDE of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', ci='sd', palette='muted')
plt.title('Bar Plot of Total Bill by Day')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

# Heatmap (Correlation Matrix)
numeric_tips = tips.select_dtypes(include=[np.number])
corr = numeric_tips.corr()

plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Heatmap of Correlation Matrix')
plt.show()

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', style='time', palette='deep')
plt.title('Scatterplot of Tips by Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.grid(True)
plt.show()

# KDE Plot with Rug Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data=tips, x='total_bill', fill=True, color='green')
sns.rugplot(data=tips, x='total_bill', color='black')
plt.title('KDE Plot of Total Bill with Rug Plot')
plt.xlabel('Total Bill')
plt.ylabel('Density')
plt.grid(True)
plt.show()

# Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='smoker', palette='coolwarm')
plt.title('Box Plot of Total Bill by Day and Smoker')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

# Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', split=True, palette='muted')
plt.title('Violin Plot of Total Bill by Day and Sex')
plt.xlabel('Day')
plt.ylabel('Total Bill')
plt.show()

# Pair Plot
sns.pairplot(tips, hue='sex', palette='coolwarm')
plt.show()
