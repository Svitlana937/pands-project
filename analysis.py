# Importing the converter package
import converter 

# Import column_creates package
import column_creates as col_crea



# Summary of the first column

with open("summary.txt", "a") as f:
  f.write(f"Summary of the first column: {col_crea.first_column_sum}\n") 
  f.write(f"Summary of the second column: {sum(col_crea.second_column_numeric)}\n")
  f.write(f"Summary of the third column: {sum(col_crea.third_column_numeric)}\n")
  f.write(f"Summary of the fourth column: {sum(col_crea.fourth_column_numeric)}\n")