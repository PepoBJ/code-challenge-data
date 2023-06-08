import csv
from flask import jsonify
from io import TextIOWrapper
from datetime import datetime
from models.base_model import BaseModel
from factories.model_factory import ModelFactory

class ChargeDataController:
    def __init__(self, database):
        self.database = database
        self.session = self.database.get_session()

    def handle_charge(self, request):
        # Obtener el nombre de la tabla desde el cuerpo del request
        table_name = request.form.get('object')

        # Obtener los archivos CSV enviados en la solicitud
        files = request.files.getlist('files')
        
        if not files:
            return jsonify({'error': "No se han enviado archivos CSV"}), 400

        try:
            for file in files:
                # Leer el archivo CSV
                text_file = TextIOWrapper(file, encoding='utf-8')
                reader = csv.reader(text_file)

                # Obtener el modelo de datos correspondiente
                model = ModelFactory().get_model(table_name)

                # Verificar si el archivo CSV está vacío
                file_empty = not any(reader)

                # Reiniciar el puntero del archivo al principio
                text_file.seek(0)

                # Verificar si el archivo CSV está vacío
                if file_empty:
                    return jsonify({'error': "El archivo CSV está vacío"}), 400

                # Obtener los nombres de las columnas del modelo
                column_names = [column.name for column in model.__table__.columns if column.name != 'process_timestamp']
                column_names = [column_names[-1]] + column_names[:-1]

                # Insertar los datos en lotes (1 a 1000 filas)
                batch = []
                count = 0

                for row in reader:
                    count += 1

                    # Convertir los valores vacíos en None
                    row = [value if value else None for value in row]
                    
                    # Verificar si la fila tiene la cantidad correcta de columnas
                    if len(row) != len(column_names):
                        return jsonify({'error': "El archivo CSV tiene un formato incorrecto"}), 400

                    # Crear un diccionario con los nombres de las columnas y los valores de la fila
                    row_dict = {column_name: value for column_name, value in zip(column_names, row)}

                    # Crear el objeto del modelo
                    obj = self.create_object(model, row_dict)
                    batch.append(obj)

                    if count == 1000:
                        # Insertar el lote en la base de datos
                        self.session.bulk_save_objects(batch)
                        batch = []
                        count = 0

                if batch:
                    # Insertar el último lote restante
                    self.session.bulk_save_objects(batch)

            self.session.commit()

            return jsonify({'message': "Datos cargados con éxito."})

        except Exception as e:
            # Manejar errores
            self.session.rollback()
            return jsonify({'error': f"Error al cargar los datos: {e}"}), 500

        finally:
            # Cerrar la sesión
            self.session.close()

    def create_object(self, model, row):
        # Agregar el campo calculado process_timestamp con la fecha actual
        row['process_timestamp'] = datetime.now()

        # Crear una instancia del modelo de datos y asignar los valores de la fila
        obj = model(**row)
        return obj
