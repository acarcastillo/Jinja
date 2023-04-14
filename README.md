# Jinja

This script uses PyMySQL to connect to the database and execute the query. It then fetches the column names and data rows, and loads the Jinja2 template from a file.

The template is rendered with the column names and data rows using the render() method. The resulting HTML is then converted to PDF using pdfkit.from_string() and saved to a file.

Note that this script requires an installation of wkhtmltopdf to convert the HTML to PDF. You can download wkhtmltopdf from the official website: https://wkhtmltopdf.org/downloads.html


Clone the fpdf_html repository from GitHub:
git clone https://github.com/briancray/fpdf-html.git

Navigate to the fpdf-html directory:
cd fpdf-html

Install fpdf_html:
python setup.py install


Verify that fpdf_html is installed correctly:
python -c "import fpdf_html; print(fpdf_html.__version__)"
This should output the version number of fpdf_html.

After you have installed fpdf_html manually, you can use it in your Python code as I showed in my previous answer.
