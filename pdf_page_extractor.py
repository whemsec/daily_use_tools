import PyPDF2

# Open the original PDF file
input_pdf = "C:\\Users\\easyo\\Desktop\\report.pdf"
output_pdf = "C:\\Users\\easyo\\Desktop\\report2.pdf"

with open(input_pdf, "rb") as file:
    reader = PyPDF2.PdfReader(file)

    # Create a writer object for the new PDF
    writer = PyPDF2.PdfWriter()

    # Add the first page (index 0) to the writer
    writer.add_page(reader.pages[0])

    # Save the first page to a new PDF
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

print("First page saved as 'first_page.pdf'")
