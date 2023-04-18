from openpyxl import Workbook
from openpyxl.styles import Style, Side

# Create a new workbook
workbook = Workbook()

# Get the active sheet
sheet = workbook.active

# Create some data for the table
data = [
    ['Name', 'Age', 'Gender'],
    ['John', 30, 'Male'],
    ['Jane', 25, 'Female'],
    ['Bob', 45, 'Male'],
]

# Add the data to the sheet
for row in data:
    sheet.append(row)

# Set the border style for the table
border_style = Style(border=Side(style='thin'))

# Set the range of cells for the table
table_range = f'A1:{chr(64+len(data[0]))}{len(data)}'

# Set the border for each cell in the table range
for row in sheet[table_range]:
    for cell in row:
        cell.style = border_style

# Save the workbook
workbook.save('my_table.xlsx')
