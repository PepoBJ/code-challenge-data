import os
import io
import pytest
from unittest import mock
from controllers.employee_hired_controller import EmployeeHiredController
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage

def test_employee_hired_route(client: FlaskClient, mock_database):
    with mock.patch.object(EmployeeHiredController, 'get_metrics') as mock_get_metrics:
        year = '2021'
        dataDummy = {
            "data": [
                {
                    "Q1": 1,
                    "Q2": 0,
                    "Q3": 0,
                    "Q4": 0,
                    "department": "Accounting",
                    "job": "Account Representative IV"
                } 
        ]}

        mock_get_metrics.return_value = dataDummy
        response = client.get(f'/employee_hired/metrics/{year}')

        assert response.status_code == 200
        assert response.json == dataDummy
