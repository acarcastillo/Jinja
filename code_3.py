import pymysql
from fpdf import FPDF
from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa

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

# Fetch the results
result = cursor.fetchall()

# Create the PDF object
pdf = FPDF()

# Create the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the query results
html = template.render(result=result)

# Convert the HTML to PDF
pdf_data = pisa.CreatePDF(html)

# Check if conversion was successful
if not pdf_data.err:
    # Add the PDF data to the PDF object
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.cell(0, 0, '')
    pdf_data.write(pdf)
    pdf.output('output.pdf', 'F')
else:
    print("Error converting HTML to PDF:", pdf_data.err)
