# Here we importing the values from the column_creates.py file
# beacause we need to use the values from the columns in the converter.py file
# Importing the column_creates package to access the columns created in that file
from column_creates import *

# Here we creating an empty list for the first column, where wil will put the values from the first column of the txt file
first_column_numeric = []
# here we starting a for loop to append same values but in float format to be able to calculate the sum of the first column
# and store them again but in first_column_numeric list with float values
for value in first_column:
    # Insert a float conversion here
    # https://www.w3schools.com/python/ref_list_append.asp
    first_column_numeric.append(float(value))

# https://docs.python.org/3/library/functions.html#sum
first_column_sum = sum(first_column_numeric)
# print("Sum of the first column:", first_column_sum)

second_column_numeric = []
for value in second_column:
    # Insert a float conversion here
    # https://www.w3schools.com/python/ref_list_append.asp
    second_column_numeric.append(float(value))

# https://docs.python.org/3/library/functions.html#sum
second_column_sum = sum(second_column_numeric)


third_column_numeric = []
for value in third_column:
    # Insert a float conversion here
    third_column_numeric.append(float(value))

third_column_sum = sum(third_column_numeric)

fourth_column_numeric = []
for value in fourth_column:
    # Insert a float conversion here
    fourth_column_numeric.append(float(value))

fourth_column_sum = sum(fourth_column_numeric)