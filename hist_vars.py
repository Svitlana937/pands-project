# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
# Importing matplotlib package for plotting the variables on histograms
import matplotlib.pyplot as plt

import os
# 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# As we need to plot four histograms, it is better to create a function that will plot the histograms for us
# def hist_plotting(variable, variable_name):
    # plt.hist(variable, variable_name)
    # os.makedirs("histograms", exist_ok=True)  # Create the directory if it doesn't exist
# 
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    # Save the histogram as a PNG file
    # plt.savefig('histogram.png')
    # plt.savefig(os.path.join("histograms", f"{variable_name}.png"))    
    # 
    # 
# 
    # plt.clf()  # Clear the current figure to avoid overlapping plots
# 

def hist_plotting(variable, variable_name):
    # Plot the histogram
    plt.hist(variable, bins=10, color='blue', edgecolor='black')  # Adjust bins as needed
    plt.title(f"Histogram of {variable_name}")
    plt.xlabel(variable_name)
    plt.ylabel("Frequency")
    
    # Ensure the directory exists
    os.makedirs("histograms", exist_ok=True)
    
    # Save the histogram as a PNG file
    plt.savefig(os.path.join("histograms", f"{variable_name}.png"))
    
    # Clear the current figure to avoid overlapping plots
    plt.clf()