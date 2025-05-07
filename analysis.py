# Importing the converter package
import converter 

# Import column_creates package
import column_creates as col_crea

# importing package with the function which draw a plot
from hist_vars import hist_plotting as hist_plotting

# creating variables for the column names
SepalLengthCm = "SepalLengthCm: "
SepalWidthCm = "SepalWidthCm: "
PetalLengthCm = "PetalLengthCm: "
PetalWidthCm = "PetalWidthCm: "

# "with open" structure for opening txt file and output sum of columns in it
with open("summary.txt", "w") as f:
  f.write(str(f'{SepalLengthCm}{converter.first_column_sum}') + "\n")
  f.write(str(f'{SepalWidthCm}{converter.second_column_sum}') + "\n")
  f.write(str(f'{PetalLengthCm}{converter.third_column_sum}') + "\n")
  f.write(str(f'{PetalWidthCm}{converter.fourth_column_sum}') + "\n")

# Plotting the histograms for the four columns
hist_plotting(converter.first_column_numeric)

