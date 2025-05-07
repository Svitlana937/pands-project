# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
# Importing matplotlib package for plotting the variables on histograms
import matplotlib.pyplot as plt

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
# As we need to plot four histograms, it is better to create a function that will plot the histograms for us
def hist_plotting(variable):
    plt.hist(variable)

    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
    # Save the histogram as a PNG file
    plt.savefig('histogram.png')