import psycopg2
import json
from datetime import date

# Establece la conexión con la base de datos
conn = psycopg2.connect(database="buscador_UTN", user="postgres", password="1111", host="localhost", port="5432")

# Crea un cursor para ejecutar consultas SQL
cur = conn.cursor()

# Ejecuta una consulta para seleccionar todos los datos de la tabla 'Resoluciones'
cur.execute("SELECT * FROM resoluciones")

# Obtiene todos los resultados de la consulta
resoluciones_data = cur.fetchall()

print(resoluciones_data)

# Convierte los datos a un diccionario
resoluciones = []

# Función para convertir fechas a strings antes de serializar a JSON
def date_handler(obj):
    if isinstance(obj, date):
        return obj.strftime("%Y-%m-%d")
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

for resolucion in resoluciones_data:
    resolucion_in = {
        "nombre": resolucion[1],
        "fecha": resolucion[2],
        "contenido": resolucion[4],
        "ubicacion": resolucion[3]
    }
    resoluciones.append(resolucion_in)


# Convertir diccionario a JSON usando la función de manejo de fechas
resoluciones_json = json.dumps(resoluciones, default=date_handler, ensure_ascii=False).strip('\ufeff')

# Guardar el JSON en un archivo si es necesario
with open("resoluciones.json", "w") as json_file:
    json_file.write(resoluciones_json)

# Cierra la conexión con la base de datos
conn.close()