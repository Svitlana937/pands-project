# Iris Dataset Analysis Project

## Overview
This project analyzes the Iris dataset by performing various data analysis and visualization tasks. The dataset consists of measurements of sepal length, sepal width, petal length, and petal width for three species of Iris flowers. The project includes generating summaries, histograms, scatter plots, and pair plots to explore the relationships between the variables.

## Features
1. **Column Summation**:
   - Calculates the sum of values for each column (e.g., Sepal Length, Sepal Width, etc.).
   - Outputs the results to a `summary.txt` file.

2. **Histogram Plotting**:
   - Generates histograms for each column to visualize the frequency distribution.
   - Saves the histograms as `.png` files in the `histograms` directory.

3. **Scatter Plotting**:
   - Creates scatter plots to explore relationships between selected pairs of columns.
   - Example: Sepal Length vs. Sepal Width, Petal Length vs. Petal Width.

4. **Pair Plotting**:
   - Generates a pair plot to visualize relationships between all four columns.
   - Saves the pair plot as a `.png` file in the `pair_plotting` directory.

## File Structure
- `analysis.py`: Main script that performs the analysis and calls plotting functions.
- `hist_vars.py`: Contains the function for generating histograms.
- `scatter_plotting.py`: Contains the function for generating scatter plots.
- `pair_plotting_extra.py`: Contains the function for generating pair plots.
- `summary.txt`: Output file containing the sum of column values.

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required libraries:
   ```bash
   pip install matplotlib seaborn pandas
   ```
3. Run the main script:
   ```bash
   python analysis.py
   ```
4. Check the output:
   - `summary.txt` for column sums.
   - `.png` files for histograms, scatter plots, and pair plots.

## Dependencies
- Python 3.x
- Matplotlib
- Seaborn
- Pandas

## Output
- **`summary.txt`**: Contains the sum of each column.
- **Histograms**: Saved in the `histograms` directory.
- **Scatter Plots**: Saved in the working directory.
- **Pair Plot**: Saved in the `pair_plotting` directory.

## References
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Iris Dataset Information](https://archive.ics.uci.edu/ml/datasets/iris)



