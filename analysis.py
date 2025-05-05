import pandas as pd                  # For handling data in DataFrames
import matplotlib.pyplot as plt      # For plotting graphs
import seaborn as sns                # For better-looking plots
import os                            # For file system operations like creating folders

# Load the Iris dataset from a CSV file
df = pd.read_csv('iris.csv')  # Assumes iris.csv is in the same directory

# Create an output directory if it doesn't already exist
os.makedirs('output', exist_ok=True)

# --- 1. Output a summary of each variable to a text file ---

# Use pandas describe() to get statistics for each column
summary = df.describe(include='all')

# Write the summary to a text file
with open('output/summary.txt', 'w') as f:
    f.write(summary.to_string())  # Convert the DataFrame to a readable string

# --- 2. Save a histogram of each variable to PNG files ---

# Loop through all columns except the last one (target) to plot histograms
for column in df.columns[:-1]:  # Excludes 'target' column
    plt.figure()  # Create a new figure for each plot
    sns.histplot(df[column], kde=True, bins=20)  # Histogram with KDE curve
    plt.title(f'Histogram of {column}')  # Title for the plot
    # Save the plot as a PNG file, replacing spaces in column names with underscores
    plt.savefig(f'output/hist_{column.replace(" ", "_")}.png')
    plt.close()  # Close the figure to free memory

# --- 3. Output a scatter plot of each pair of variables ---

# Use seaborn's pairplot to create scatter plots for all variable pairs
# hue='target' colors the points by species
sns.pairplot(df, hue='target', plot_kws={'alpha': 0.7})  # alpha adds transparency
plt.savefig('output/scatter_matrix.png')  # Save the entire grid as one image
plt.close()  # Close the plot
