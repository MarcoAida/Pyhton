import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the data
df = pd.read_csv('voti.csv')

# Display descriptive statistics
print(df.describe())

# Plot histograms of all columns
df.hist(figsize=(10, 8))

# Ensure the directory exists
os.makedirs('./parzialeSO', exist_ok=True)

# Save the plot as an image
plt.savefig('histograms.png')

# Show the plot
plt.show()
