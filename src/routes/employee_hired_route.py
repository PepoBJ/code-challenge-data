from flask import Blueprint, request, current_app
from controllers import EmployeeHiredController

employee_hired_metrics_route_bp = Blueprint('employee_hired_metrics', __name__)

@employee_hired_metrics_route_bp.route('/employee_hired/metrics/<int:year>', methods=['GET'])
def employee_hired_metrics_data_route(year):
    database = current_app.config.get('DATABASE_INSTANCE')
    controller = EmployeeHiredController(database)

    return controller.get_metrics(request, year)

