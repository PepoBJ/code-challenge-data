import pyodbc

def create_procedures(connection_string):
    try:
        # Conectarse a la base de datos
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        try:
            # Crear procedimiento 'GetEmployeeHiredByQuarterMetrics'
            cursor.execute('''
                CREATE PROCEDURE GetEmployeeHiredByQuarterMetrics
                    @year INT
                AS
                BEGIN
                    SELECT department, job,
                        SUM(CASE WHEN DATEPART(QUARTER, hire_datetime) = 1 THEN 1 ELSE 0 END) AS Q1,
                        SUM(CASE WHEN DATEPART(QUARTER, hire_datetime) = 2 THEN 1 ELSE 0 END) AS Q2,
                        SUM(CASE WHEN DATEPART(QUARTER, hire_datetime) = 3 THEN 1 ELSE 0 END) AS Q3,
                        SUM(CASE WHEN DATEPART(QUARTER, hire_datetime) = 4 THEN 1 ELSE 0 END) AS Q4
                    FROM hired_employees
                    INNER JOIN departments ON hired_employees.department_id = departments.id
                    INNER JOIN jobs ON hired_employees.job_id = jobs.id
                    WHERE YEAR(hire_datetime) = @year
                    GROUP BY department, job
                    ORDER BY department, job;
                END

            ''')

            # Crear procedimiento 'GetDepartmentsAboveAverageMetrics'
            cursor.execute('''
                CREATE PROCEDURE GetDepartmentsAboveAverageMetrics
                    @year INT
                AS
                BEGIN
                    WITH EmployeeCounts AS (
                        SELECT department_id, COUNT(*) AS hired,
                            AVG(COUNT(*)) OVER () AS avg_hired
                        FROM hired_employees
                        WHERE YEAR(hire_datetime) = @year
                        GROUP BY department_id
                    )
                    SELECT d.id, d.department, e.hired
                    FROM EmployeeCounts e
                    JOIN departments d ON d.id = e.department_id
                    WHERE e.hired > e.avg_hired
                    ORDER BY e.hired DESC;
                END
            ''')

            # Confirmar los cambios
            conn.commit()
            print("Procesimientos almacenados creados con éxito.")

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
