import matplotlib.pyplot as plt
import pandas as pd
import os


# Function to adapt the values in the 'Parz2/totale' column
def adapt_parz2(value):
    if pd.isna(value):
        return value
    try:
        num, denom = map(int, value.split('/'))
        if denom == 30:
            return value  # Return the value unchanged if the denominator is already 30
        return f"{num*2}/{denom*2}"
    except ValueError:
        return value


# Function to calculate the average of the values before the '/' in both columns
def calculate_average(row):
    parz1 = row['Parz1']
    parz2_totale = row['Parz2/totale']

    try:
        parz1_value = int(parz1.split('/')[0]) if pd.notna(parz1) else None
    except AttributeError:
        parz1_value = None

    try:
        parz2_value = int(
            parz2_totale.split('/')[0]) if pd.notna(parz2_totale) else None
    except AttributeError:
        parz2_value = None

    values = [parz1_value, parz2_value]
    values = [v for v in values if v is not None]

    if values:
        return sum(values) / len(values)
    return None  # Use None instead of 'NA' for easier comparison


# Function to extract the numeric value before '/' in a column
def extract_value(value):
    if pd.isna(value):
        return None
    try:
        return int(value.split('/')[0])
    except (ValueError, AttributeError):
        return None


# Load the data
df = pd.read_csv('voti.csv')

# Apply the adaptation function to the 'Parz2/totale' column
df['Parz2/totale'] = df['Parz2/totale'].apply(adapt_parz2)

# Apply the calculate_average function to each row and create a new column 'Average'
df['Average'] = df.apply(calculate_average, axis=1)

# Extract numeric values for Parz1 and Parz2
df['Parz1_numeric'] = df['Parz1'].apply(extract_value)
df['Parz2_numeric'] = df['Parz2/totale'].apply(extract_value)

# Count how many students have a final average score greater than 18
num_students_above_18 = df['Average'].dropna().apply(lambda x: x > 18).sum()

# Count how many students have a Parz1 score greater than 18
num_students_above_18_Parz1 = df['Parz1_numeric'].dropna().apply(
    lambda x: x > 18).sum()

# Count how many students have a Parz2 score greater than 18
num_students_above_18_Parz2 = df['Parz2_numeric'].dropna().apply(
    lambda x: x > 18).sum()

# Print the results
print(
    f"Number of students with a final average score greater than 18: {num_students_above_18}"
)
print(
    f"Number of students with Parz1 score greater than 18: {num_students_above_18_Parz1}"
)
print(
    f"Number of students with Parz2 score greater than 18: {num_students_above_18_Parz2}"
)

# Save the updated data back to a CSV file
df.to_csv('voti_adapted.csv', index=False, na_rep='NA')

# Display descriptive statistics
print(df.describe())

# Plot histograms of all columns
df.hist(figsize=(10, 8))

# Ensure the directory exists
os.makedirs('./parzialeSO_2', exist_ok=True)

# Save the plot as an image
plt.savefig('./parzialeSO_2/histograms.png')

# Show the plot
plt.show()
