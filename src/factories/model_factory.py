from models import Department, Job, Employee

class ModelFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_model(self, table_name):
        # Obtener el modelo de datos correspondiente según el nombre de la tabla

        if table_name == "departments":
            return Department
        elif table_name == "jobs":
            return Job
        elif table_name == "employees":
            return Employee
        else:
            raise ValueError("Tabla desconocida: " + str(table_name))
