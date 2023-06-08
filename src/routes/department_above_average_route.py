from flask import Blueprint, request, current_app
from controllers import DepartmentAboveAverageController

department_above_average_metrics_route_bp = Blueprint('department_above_average_metrics', __name__)

@department_above_average_metrics_route_bp.route('/department_above_average/metrics/<int:year>', methods=['GET'])
def department_above_average_metrics_data_route(year):
    database = current_app.config.get('DATABASE_INSTANCE')
    controller = DepartmentAboveAverageController(database)

    return controller.get_metrics(request, year)
