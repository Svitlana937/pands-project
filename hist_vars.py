# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
# Importing matplotlib package for plotting the variables on histograms
import matplotlib.pyplot as plt

import os
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# As we need to plot four histograms, it is better to create a function that will plot the histograms for us
def hist_plotting(variable, variable_name):
    # Plot the histogram
    plt.hist(variable, bins=10, color='blue', edgecolor='black')  # Adjust bins as needed
    
    # Add title and labels
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
    plt.title(f"Histogram of {variable_name}")

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html

    plt.xlabel(variable_name)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
    plt.ylabel("Frequency")
    
    # Ensure the directory exists
    # https://docs.python.org/3/library/os.html#os.makedirs
    os.makedirs("histograms", exist_ok=True)
    
    # Save the histogram as a PNG file to a folder named "histograms"
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    plt.savefig(os.path.join("histograms", f"{variable_name}.png"))
    
    # Clear the current figure to avoid overlapping plots
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.clf.html
    plt.clf()