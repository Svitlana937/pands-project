# Iris Dataset Analysis Project

## Overview
This project analyzes the famous Iris dataset by performing the following tasks:
- Summing up the values of specific columns in the dataset.
- Generating histograms for each column to visualize the data distribution.
- Creating scatter plots to explore relationships between columns.

## Features
1. **Column Summation**:
   - Calculates the sum of values for each column (e.g., Sepal Length, Sepal Width, etc.).
   - Outputs the results to a `summary.txt` file.

2. **Histogram Plotting**:
   - Generates histograms for each column to visualize the frequency distribution.
   - Saves the histograms as `.png` files.

3. **Scatter Plotting**:
   - Creates scatter plots to explore relationships between selected columns.
   - Example: Sepal Length vs. Sepal Width.

## File Structure
- `analysis.py`: Main script that performs the analysis and calls plotting functions.
- `hist_vars.py`: Contains the function for generating histograms.
- `scatter_plotting.py`: Contains the function for generating scatter plots.
- `summary.txt`: Output file containing the sum of column values.

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required libraries:
   ```bash
   pip install matplotlib