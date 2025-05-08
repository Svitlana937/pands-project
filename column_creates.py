# Importing the iris_data_load package, with lines variable where we stored the data from the iris dataset
# https://docs.python.org/3/tutorial/modules.html#packages
# https://www.geeksforgeeks.org/how-to-import-other-python-files/
from iris_data_load import *


# Each iteration for loop takes a line from the lines variable and splits it by comma
# and appends the first item to the first_column list
# this way we are creating a list of the first column values
# https://www.w3schools.com/python/ref_list_append.asp
first_column = []
for line in lines:
    # https://www.w3schools.com/python/ref_string_strip.asp
    if line.strip():  # Skip empty lines
        first_column.append(line.split(',')[0])


# Extracting the second column 
second_column = []
for line in lines:
    if line.strip():  # Skip empty lines
        second_column.append(line.split(',')[1])


# Extracting the third column 
third_column = []
for line in lines:
    if line.strip():  # Skip empty lines
        third_column.append(line.split(',')[2])


# Extracting the fourth column
fourth_column = []
for line in lines:
    if line.strip():  # Skip empty lines
        fourth_column.append(line.split(',')[3])