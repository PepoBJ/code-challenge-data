import pyodbc

def drop_procedures(connection_string):
    try:
        # Conectarse a la base de datos
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        try:
            # Eliminar 'GetEmployeeHiredByQuarterMetrics'
            cursor.execute('''
                DROP PROCEDURE GetEmployeeHiredByQuarterMetrics
            ''')
            
            # Eliminar 'GetDepartmentsAboveAverageMetrics'
            cursor.execute('''
                DROP PROCEDURE GetDepartmentsAboveAverageMetrics
            ''')

            # Confirmar los cambios
            conn.commit()
            print("Procesdimientos borrados con éxito.")

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
