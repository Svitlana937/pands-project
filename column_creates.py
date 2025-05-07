# Extracting the first column 
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