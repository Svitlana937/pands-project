# Importing the converter package
import converter 

# Import column_creates package
import column_creates as col_crea

# importing package with the function which draw a plot
from hist_vars import hist_plotting as hist_plotting

# importing package with the function which draw a scatter plot
from scatter_plotting import scatter_plotting as scatter_plotting

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
hist_plotting(converter.first_column_numeric, "Sepal Length Histogram")
hist_plotting(converter.second_column_numeric, "Sepal Width Histogram")
hist_plotting(converter.third_column_numeric, "Petal Length Histogram")
hist_plotting(converter.fourth_column_numeric, "Petal Width Histogram")

# Plotting the scatter plot for the first two columns
scatter_plotting(converter.first_column_numeric, converter.second_column_numeric,
                title="Sepal Length vs Sepal Width", xlabel="Sepal Length (cm)", ylabel="Sepal Width (cm)")
scatter_plotting(converter.third_column_numeric, converter.fourth_column_numeric,
                title="Petal Length vs Petal Width", xlabel="Petal Length (cm)", ylabel="Petal Width (cm)")
