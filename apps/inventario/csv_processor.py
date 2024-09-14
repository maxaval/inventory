import csv
from io import TextIOWrapper

class CsvProcessor:
    def __init__(self, model, csv_file, field_mapping):
        self.model = model
        self.csv_file = csv_file
        self.field_mapping = field_mapping

    def process_csv(self):
        content = TextIOWrapper(self.csv_file, encoding='utf-8')

        reader = csv.DictReader(content)
        total_filas = sum(1 for row in reader)
        content.seek(0)  # Reiniciar el puntero del archivo al principio

        # Omitir la primera fila (encabezado)
        next(reader, None)

        for i, row in enumerate(reader):
            # Procesar los datos según el mapeo de campos
            datos_modelo = {campo_modelo: row.get(campo_csv, '') for campo_csv, campo_modelo in self.field_mapping.items()}

            # Crear una instancia del modelo y guardarla en la base de datos
            instancia_modelo = self.model(**datos_modelo)
            instancia_modelo.save()

            # Calcular y devolver el progreso en porcentaje
            progreso = int((i + 1) / total_filas * 100)
            yield progreso
            