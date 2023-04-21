import os
from openpyxl import load_workbook

folder_path = '/ruta/de/la/carpeta'

# Crear una lista de todos los archivos en la carpeta con extensión .xlsx
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Contar el número de archivos con un tamaño mayor a 100KB
count = 0
for file in files:
    file_path = os.path.join(folder_path, file)
    size = os.path.getsize(file_path)
    if size > 100000:
        count += 1

print(f'Hay {count} archivos mayores de 100KB en la carpeta {folder_path}.')
