import pymysql
from jinja2 import Template
import pdfkit

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='password',
                             db='database_name')

# Create a cursor object
cursor = connection.cursor()

# Execute the query
query = "SELECT * FROM table_name"
cursor.execute(query)

# Fetch the column names
cols = [col[0] for col in cursor.description]

# Fetch the data rows
rows = cursor.fetchall()

# Load the Jinja2 template
with open('template.html') as f:
    template = Template(f.read())

# Render the template with the SQL data
html = template.render(cols=cols, rows=rows)

# Convert the HTML to PDF
pdfkit.from_string(html, 'output.pdf')
