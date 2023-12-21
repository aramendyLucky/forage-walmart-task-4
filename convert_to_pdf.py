from nbconvert import PDFExporter
import nbformat

# Lee el notebook
with open('populate_database.ipynb', 'r', encoding='utf-8') as notebook_file:
    notebook_content = nbformat.read(notebook_file, as_version=4)

# Crea un exportador PDF
pdf_exporter = PDFExporter()

# Configura el exportador para que incluya la información del código
pdf_exporter.exclude_input = False

# Exporta el notebook a PDF
pdf_data, _ = pdf_exporter.from_notebook_node(notebook_content)

# Guarda el PDF
with open('populate_database.pdf', 'wb') as pdf_file:
    pdf_file.write(pdf_data)
