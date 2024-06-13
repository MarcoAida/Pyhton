import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
df = pd.read_csv('votiLab.csv')

#all
# Display descriptive statistics
#print(df.describe())

# Plot histograms of all columns
#df.hist(figsize=(10, 8))

#without 0 row
# Filter out rows where all values are zero (excluding the first column which is an identifier)
filtered_df = df[(df.iloc[:, 1:] != 0).any(axis=1)]

print(filtered_df.describe())

# Plot histograms of all columns
filtered_df.hist(figsize=(10, 8))

# Ensure the directory exists
os.makedirs('./parzialeSO', exist_ok=True)

# Save the plot as an image
plt.savefig('histograms.png')

# Show the plot
plt.show()
