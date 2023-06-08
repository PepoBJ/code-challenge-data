import sys
from flask import Flask, jsonify

from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint

from config import environment as env
from config.database import Database

from routes.charge_data_route import charge_route_bp
from routes.department_above_average_route import department_above_average_metrics_route_bp
from routes.employee_hired_route import employee_hired_metrics_route_bp

from _migrations.create_structure import create_tables
from _migrations.drop_structure import drop_tables
from _migrations.create_procedures_metrics import create_procedures
from _migrations.drop_procedures_metrics import drop_procedures

def create_app():
    app = Flask(__name__)
    database = Database()
    app.config['DATABASE_INSTANCE'] = database

    app.register_blueprint(charge_route_bp)
    app.register_blueprint(department_above_average_metrics_route_bp)
    app.register_blueprint(employee_hired_metrics_route_bp)

    ### swagger ###
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Data Challenge"
        }
    )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    ### end swagger ###

    return app

def initialize_db():
    create_tables(env.CONNECTION_STRING)
    create_procedures(env.CONNECTION_STRING)

def clean_db():
    drop_tables(env.CONNECTION_STRING)
    drop_procedures(env.CONNECTION_STRING)

def initialize_procedures():
    create_procedures(env.CONNECTION_STRING)

def clean_procedures():
    drop_procedures(env.CONNECTION_STRING)

def start_app():
    app = create_app()
    app.run(host=env.HOST, port=env.PORT, debug=env.DEBUG)

def run():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'db_init':
            initialize_db()
        elif command == 'db_clean':
            clean_db()
        elif command == 'db_procedure_init':
            initialize_procedures()
        elif command == 'db_procedure_clean':
            clean_procedures()
        else:
            raise ValueError(f"Invalid argument '{command}' to initialize the database")
    else:
        start_app()

if __name__ == "__main__":
    run()
