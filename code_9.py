import pyodbc
import openpyxl

# Connect to the database
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=mydatabase;UID=myusername;PWD=mypassword')

# Execute a SQL query and retrieve the results
cursor = conn.cursor()
sql_query = "SELECT * FROM mytable"
cursor.execute(sql_query)
results = cursor.fetchall()

# Create a new workbook and worksheet using openpyxl
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Write the column headers to the worksheet
columns = [column[0] for column in cursor.description]
worksheet.append(columns)

# Write the data to the worksheet
for row in results:
    worksheet.append(row)

# Create an OpenpyxlWriter object and save the workbook to disk
writer = openpyxl.writer.excel.WorkbookWriter(workbook)
writer.save_workbook('my_excel_file.xlsx')

# Close the database connection
conn.close()
