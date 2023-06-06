from flask import Blueprint, request, current_app
from handlers import ChargeData

charge_route_bp = Blueprint('charge', __name__)

@charge_route_bp.route('/charge', methods=['POST'])
def charge_data_route():
    database = current_app.config.get('DATABASE_INSTANCE')
    charge_data_handler = ChargeData(database)

    return charge_data_handler.handle_charge(request)
