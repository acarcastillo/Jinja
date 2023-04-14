from fpdf import FPDF
import sqlite3
import jinja2
import re

# Define a subclass of FPDF with HTML support
class MyFPDF(FPDF):
    pass

# Step 1: Query the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM mytable')
data = cursor.fetchall()

# Step 2: Load the jinja2 template from a file
with open('mytemplate.html') as f:
    template_string = f.read()
template = jinja2.Template(template_string)

# Step 3: Render the jinja2 template
html_string = template.render(data=data)

# Step 4: Generate the PDF file
pdf = MyFPDF()
pdf.add_page()

# Parse the HTML string and manually create a table in the PDF
pdf.set_font('Arial', '', 14)
pdf.cell(0, 10, 'My PDF', 0, 1)
pdf.ln(10)
pdf.set_font('Arial', '', 12)

# Find all table rows in the HTML string using a regular expression
pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
rows = pattern.findall(html_string)

# Loop over the rows and create a table in the PDF
for row in rows:
    # Find all table cells in the row using another regular expression
    cell_pattern = re.compile(r'<td>(.*?)</td>', re.DOTALL)
    cells = cell_pattern.findall(row)
    for cell in cells:
        pdf.cell(60, 10, cell, 1)
    pdf.ln()

pdf.output('myoutput.pdf')
