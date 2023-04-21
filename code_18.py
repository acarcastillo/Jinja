import os
from openpyxl import load_workbook

folder_path = '/ruta/de/la/carpeta'

# Crear una lista de todos los archivos en la carpeta con extensión .xlsx
files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Inicializar contadores para cada criterio
mayores_100KB_count = 0
entre_50KB_100KB_count = 0
menores_50KB_count = 0

# Iterar sobre cada archivo y actualizar los contadores correspondientes
for file in files:
    file_path = os.path.join(folder_path, file)
    size = os.path.getsize(file_path)
    if size > 100000:
        mayores_100KB_count += 1
    elif 50000 <= size <= 100000:
        entre_50KB_100KB_count += 1
    else:
        menores_50KB_count += 1

# Imprimir los contadores
print(f'Archivos mayores a 100KB: {mayores_100KB_count}')
print(f'Archivos entre 50KB y 100KB: {entre_50KB_100KB_count}')
print(f'Archivos menores a 50KB: {menores_50KB_count}')
