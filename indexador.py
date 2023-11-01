import os
from PyPDF2 import PdfReader
import json

directorio_pdfs = "/Users/usuario/Downloads/RESOLUCIONES DE CONSEJO DIRECTIVO/2023"

indexed_data = []

for filename in os.listdir(directorio_pdfs):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(directorio_pdfs, filename)
        with open(pdf_path, "rb") as file:
            pdf_reader = PdfReader(file)
            text = []
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text.append(page.extract_text())

            # Extrae el nombre del archivo (sin la extensión) y la ubicación
            nombre = os.path.splitext(filename)[0]
            ubicacion = nombre

            # Obtén la fecha del PDF (puedes usar métodos específicos según el formato del texto extraído)
            # Supongamos que la fecha se encuentra en la primera página del PDF
            fecha = "2023"

            # Convierte el texto extraído en un solo string
            contenido = "\n".join(text)
            contenido = contenido.replace("\t", "").replace("  ", "").replace("\n", "")

            # Almacena los datos en la lista indexed_data como un diccionario
            indexed_data.append({
                "nombre": nombre,
                "fecha": fecha,
                "contenido": contenido,
                "ubicacion": ubicacion
            })

# Almacena el diccionario en un archivo JSON
with open("indexed_data.json", "w", encoding="utf-8") as json_file:
    json.dump(indexed_data, json_file, ensure_ascii=False, indent=4)

print("Indexación completa. Los datos se han almacenado en indexed_data.json")


