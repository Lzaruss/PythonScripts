import json
filename = ''

# Abrir el archivo en modo lectura
with open(filename, "r") as file:
  # Leer el contenido del archivo y almacenarlo en una lista
  lines = file.readlines()

# Convertir la lista a formato JSON
json_data = json.dumps(lines)

# Guardar el contenido JSON en un nuevo archivo
with open("blocklist.json", "w") as file:
  file.write(json_data)