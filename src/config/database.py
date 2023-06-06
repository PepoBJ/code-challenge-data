from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import environment as env

class Database:
    def __init__(self):
        connection_string = f"mssql+pyodbc:///?odbc_connect={env.CONNECTION_STRING}"
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()