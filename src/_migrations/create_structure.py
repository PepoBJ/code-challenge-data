import pyodbc

def create_tables(connection_string):
    try:
        # Conectarse a la base de datos
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        try:
            # Crear la tabla 'departments'
            cursor.execute('''
                CREATE TABLE departments (
                    id INT,
                    department NVARCHAR(255),
                    process_timestamp DATETIME,
                    PRIMARY KEY (id)
                )
            ''')

            # Crear la tabla 'jobs'
            cursor.execute('''
                CREATE TABLE jobs (
                    id INT,
                    job NVARCHAR(255),
                    process_timestamp DATETIME,
                    PRIMARY KEY (id)
                )
            ''')

            # Crear la tabla 'hired_employees'
            cursor.execute('''
                CREATE TABLE hired_employees (
                    id INT,
                    name NVARCHAR(255),
                    hire_datetime DATETIME,
                    department_id INT NULL,
                    job_id INT NULL,
                    process_timestamp DATETIME,
                    PRIMARY KEY (id),
                    FOREIGN KEY (department_id) REFERENCES departments(id),
                    FOREIGN KEY (job_id) REFERENCES jobs(id)
                )
            ''')

            # Confirmar los cambios
            conn.commit()
            print("Estructura de tablas creada con éxito.")

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
