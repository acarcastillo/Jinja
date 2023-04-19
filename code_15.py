# Specify the range of cells to sum
cell_range = ws['A9:AH13']

# Initialize a list to store the sums of each column
column_sums = [0] * cell_range.max_column

# Iterate over each row in the range and sum the values in each column
for row in cell_range:
    for i, cell in enumerate(row):
        # Only sum values for columns with numeric data
        if isinstance(cell.value, (int, float)):
            column_sums[i] += cell.value

# Output the sums for each column
for i, col_sum in enumerate(column_sums):
    print(f"Sum of column {ws.cell(row=8, column=i+1).value}: {col_sum}")
