# Getting an access to iris dataset
# https://docs.python.org/3/tutorial/inputoutput.html
with open('iris/iris.data', 'r') as f:
    read_data = f.read()

# Checking if we got the access to the file
# print(read_data)    

# Splitting the data into lines
lines = read_data.strip().split('\n')


# Extracting the first column 
first_column = []
for line in lines:
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


