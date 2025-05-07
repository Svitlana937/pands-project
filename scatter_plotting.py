# Importing scatter package for plotting the variables on scatter plot
import matplotlib.pyplot as plt

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html


def scatter_plotting(variable_one, variable_two, title="Scatter Plot", xlabel="Variable One", ylabel="Variable Two"):
    plt.scatter(variable_one, variable_two, c='blue', alpha=0.5)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig('scatter_plot.png')