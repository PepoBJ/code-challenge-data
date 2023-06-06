import sys
from flask import Flask
from config import environment as env
from config.database import Database

from routes.test_route import test_route_bp
from routes.charge_route import charge_route_bp

from _migrations.create_structure import create_tables
from _migrations.drop_structure import drop_tables

def create_app():
    app = Flask(__name__)
    database = Database()
    app.config['DATABASE_INSTANCE'] = database

    app.register_blueprint(test_route_bp)
    app.register_blueprint(charge_route_bp)
    return app

def run():
    if len(sys.argv) > 1 and sys.argv[1] == 'db_init':
        create_tables(env.CONNECTION_STRING)
    elif len(sys.argv) > 1 and sys.argv[1] == 'db_clean':
        drop_tables(env.CONNECTION_STRING)
    else:
        app = create_app()
        app.run(host=env.HOST, port=env.PORT, debug=env.DEBUG)

if __name__ == "__main__":
    run()
