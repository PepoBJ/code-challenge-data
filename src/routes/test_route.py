from flask import Blueprint

test_route_bp = Blueprint('test', __name__)

@test_route_bp.route('/test', methods=['GET'])
def other_route():
    return "Test Route"
