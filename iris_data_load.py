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