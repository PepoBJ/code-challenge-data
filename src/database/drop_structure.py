import pyodbc

def drop_tables(connection_string):
    try:
        # Conectarse a la base de datos
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        try:
            # Crear la tabla 'hired_employees'
            cursor.execute('''
                DROP TABLE hired_employees
            ''')
            
            # Crear la tabla 'departments'
            cursor.execute('''
                DROP TABLE departments
            ''')

            # Crear la tabla 'jobs'
            cursor.execute('''
                DROP TABLE jobs
            ''')

            # Confirmar los cambios
            conn.commit()
            print("Estructura de tablas borrada con éxito.")

        except pyodbc.Error as e:
            # Manejar errores de consulta SQL
            conn.rollback()
            print(f"Error al ejecutar consulta SQL: {e}")

        finally:
            # Cerrar la conexión
            conn.close()

    except pyodbc.Error as e:
        # Manejar errores de conexión
        print(f"Error al conectar a la base de datos: {e}")
