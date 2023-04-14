from fpdf import FPDF

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()

    def header(self):
        # Set up the font
        self.set_font('Arial', 'B', 16)
        # Add the title
        self.cell(0, 10, 'My Document', 0, 1, 'C')

    def footer(self):
        # Add the page number
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')

    def content(self):
        # Set up the font
        self.set_font('Arial', '', 12)
        # Add some text
        self.multi_cell(0, 10, 'This is some sample text.')

# Create a PDF object
pdf = PDF()
pdf.content()

# Output the PDF
pdf.output('output.pdf', 'F')
