import os
from openpyxl import load_workbook

folder_path = '/ruta/de/la/carpeta'

# Crear una lista de todos los archivos en la carpeta con extensión .xlsx
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Crear un diccionario para almacenar los archivos que cumplen con diferentes criterios
file_dict = {'mayores_100KB': [], 'entre_50KB_100KB': [], 'menores_50KB': []}

# Iterar sobre cada archivo y agregarlo al diccionario correspondiente
for file in files:
    file_path = os.path.join(folder_path, file)
    size = os.path.getsize(file_path)
    if size > 100000:
        file_dict['mayores_100KB'].append(file)
    elif 50000 <= size <= 100000:
        file_dict['entre_50KB_100KB'].append(file)
    else:
        file_dict['menores_50KB'].append(file)

# Imprimir el diccionario
print(file_dict)
