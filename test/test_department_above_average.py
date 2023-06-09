import os
import io
import pytest
from unittest import mock
from controllers.department_above_average_controller import DepartmentAboveAverageController
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage

def test_department_above_average_route(client: FlaskClient, mock_database):
    with mock.patch.object(DepartmentAboveAverageController, 'get_metrics') as mock_get_metrics:
        year = '2021'
        dataDummy = {
            "data": [
                {
                    "department": "Support",
                    "hired": 221,
                    "id": 8
                },
                {
                    "department": "Engineering",
                    "hired": 208,
                    "id": 5
                }
        ]}

        mock_get_metrics.return_value = dataDummy
        response = client.get(f'/department_above_average/metrics/{year}')

        assert response.status_code == 200
        assert response.json == dataDummy
