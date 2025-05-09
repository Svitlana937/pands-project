# Importing seaborn package for plotting 
# https://seaborn.pydata.org/tutorial/introduction.html#  
# is a matrix of graphs that enables 
# the visualization of the relationship between each pair of variables in a dataset
import seaborn as sns

# https://www.w3schools.com/python/pandas/pandas_getting_started.asp
# Importing pandas package for data manipulation and analysis
import pandas as pd


# Importing matplotlib package for plotting the variables on histograms
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html
import matplotlib.pyplot as plt


import os
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

# Creating a function which will create a pair plot for the four columns
# https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot
def pair_plotting(data):
    df = pd.DataFrame(data)

    # Ensure the directory exists
    # https://docs.python.org/3/library/os.html#os.makedirs
    os.makedirs("pair_plotting", exist_ok=True)

    # https://seaborn.pydata.org/generated/seaborn.pairplot.html#seaborn-pairplot
    sns.pairplot(df)
    # https://seaborn.pydata.org/tutorial/color_palettes.html#color-palettes        
    plt.savefig(os.path.join("pair_plotting", "pair_plot.png"))      
    # plt.savefig(os.path.join("histograms", f"{'pair'}.png"))
    # plt.clf()