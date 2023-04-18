import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect('example.db')

# Define your SQL query
query = "SELECT * FROM my_table"

# Execute the query and store the result in a Pandas dataframe
df = pd.read_sql_query(query, conn)

# Define the file path for the Excel file
file_path = 'my_data.xlsx'

# Export the dataframe to Excel
df.to_excel(file_path, index=False)

# Close the database connection
conn.close()
