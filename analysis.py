# Importing the converter package
import converter 

# Import column_creates package
import column_creates

# Getting an access to iris dataset
# https://docs.python.org/3/tutorial/inputoutput.html
with open('iris/iris.data', 'r') as f:
    read_data = f.read()

# Checking if we got the access to the file
# print(read_data)    

# Splitting the data into lines
# https://www.w3schools.com/python/ref_string_strip.asp
# https://www.w3schools.com/python/ref_string_rsplit.asp
lines = read_data.strip().split('\n')


# Summary of the first column

with open("summary.txt", "a") as f:
  f.write(f"Summary of the first column: {first_column_sum}\n") 
  f.write(f"Summary of the second column: {sum(second_column_numeric)}\n")
  f.write(f"Summary of the third column: {sum(third_column_numeric)}\n")
  f.write(f"Summary of the fourth column: {sum(fourth_column_numeric)}\n")