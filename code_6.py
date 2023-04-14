from jinja2 import Environment, FileSystemLoader
import sqlite3
import weasyprint

# Connect to database and execute query
conn = sqlite3.connect('example.db')
cur = conn.cursor()
cur.execute('SELECT column1, column2, column3 FROM table1')

# Get query results
result = cur.fetchall()

# Set up Jinja2 environment and load template file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render template with query results
html = template.render(result=result)

# Generate PDF from HTML content and output the file
weasyprint.HTML(string=html).write_pdf('output.pdf')
