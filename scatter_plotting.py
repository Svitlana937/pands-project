# Importing scatter package for plotting the variables on scatter plot
import matplotlib.pyplot as plt

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorial-introductory-pyplot-py
# importing os package for creating directories and saving files
import os


def scatter_plotting(variable_one, variable_two, title="Scatter Plot", xlabel="Variable One", ylabel="Variable Two"):
    # Create a scatter plot folder if it doesn't exist
    # https://docs.python.org/3/library/os.html#os.makedirs
    os.makedirs("scatter_plots", exist_ok=True)

    plt.scatter(variable_two, variable_one, c='blue', alpha=0.5, label = xlabel)
    plt.scatter(variable_one, variable_two, c='red', alpha=0.5, label = ylabel)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)    
    
    plt.savefig(os.path.join('scatter_plots', f'{xlabel}_vs_{ylabel}.png'), format='png')