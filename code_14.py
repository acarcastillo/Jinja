from openpyxl.utils import column_index_from_string, get_column_letter

cell1 = sheet['A1']  # starting cell

for i in range(10):
    # get the row and column indices of the starting cell
    row_idx, col_idx = cell1.row, column_index_from_string(cell1.column)

    # increment the column index to move one cell to the right
    col_idx += 1

    # convert the new column index back to a letter
    col_letter = get_column_letter(col_idx)

    # combine the new row and column indices to get the coordinate of the new cell
    cell2_coord = f"{col_letter}{row_idx}"

    print(cell2_coord)  # prints the coordinate of the cell to the right of the previous cell
    cell1 = sheet[cell2_coord]  # set the starting cell to the new cell for the next iteration
