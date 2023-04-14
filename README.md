# Jinja

This script uses PyMySQL to connect to the database and execute the query. It then fetches the column names and data rows, and loads the Jinja2 template from a file.

The template is rendered with the column names and data rows using the render() method. The resulting HTML is then converted to PDF using pdfkit.from_string() and saved to a file.

Note that this script requires an installation of wkhtmltopdf to convert the HTML to PDF. You can download wkhtmltopdf from the official website: https://wkhtmltopdf.org/downloads.html
