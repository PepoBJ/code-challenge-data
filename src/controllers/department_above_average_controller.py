from flask import jsonify
from sqlalchemy import text
from models.base_model import BaseModel
from utils.response_util import ResponseUtil

class DepartmentAboveAverageController:
    def __init__(self, database):
        self.database = database
        self.session = self.database.get_session()

    def get_metrics(self, request, year):
        try:
            resultDepartments = self.session.execute(text("EXEC GetDepartmentsAboveAverageMetrics :year"), {"year": year})

            response = {
                'data': ResponseUtil.build_results_dict(resultDepartments)
            }

            return jsonify(response)

        except Exception as e:
            return jsonify({'error': str(e)}), 500