import nbformat

# Lee el script Python
with open('populate_database.py', 'r') as script_file:
    script_content = script_file.read()

# Crea un nuevo notebook
notebook_content = nbformat.v4.new_notebook()
notebook_content['cells'] = [nbformat.v4.new_code_cell(script_content)]

# Guarda el notebook como .ipynb
with open('populate_database.ipynb', 'w', encoding='utf-8') as notebook_file:
    nbformat.write(notebook_content, notebook_file)
