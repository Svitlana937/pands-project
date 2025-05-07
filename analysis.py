# Importing the converter package
import converter 

# Import column_creates package
import column_creates as col_crea

SepalLengthCm = "SepalLengthCm: "
SepalWidthCm = "SepalWidthCm: "
PetalLengthCm = "PetalLengthCm: "
PetalWidthCm = "PetalWidthCm: "
# Summary of the first column
# 
with open("summary.txt", "w") as f:
  f.write(str(f'{SepalLengthCm}{converter.first_column_sum}') + "\n")
  f.write(str(f'{SepalWidthCm}{converter.second_column_sum}') + "\n")
  f.write(str(f'{PetalLengthCm}{converter.third_column_sum}') + "\n")
  f.write(str(f'{PetalWidthCm}{converter.fourth_column_sum}') + "\n")


