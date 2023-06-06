import sys
import config
from flask import Flask
from routes.test_route import test_route_bp
from database.create_structure import create_tables
from database.drop_structure import drop_tables

def create_app():
    app = Flask(__name__)
    app.register_blueprint(test_route_bp)
    return app

def run():
    if len(sys.argv) > 1 and sys.argv[1] == 'db_init':
        create_tables(config.CONNECTION_STRING)
    elif len(sys.argv) > 1 and sys.argv[1] == 'db_clean':
        drop_tables(config.CONNECTION_STRING)
    else:
        app = create_app()
        app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

if __name__ == "__main__":
    run()
