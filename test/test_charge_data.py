import os
import io
import pytest
from unittest import mock
from controllers.charge_data_controller import ChargeDataController
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.datastructures import FileStorage

def test_charge_data_route_upload(client: FlaskClient, mock_database):
    controller = ChargeDataController(mock_database)

    table_name = 'departments'
    csv_path = os.path.abspath('./test/resources/departments.csv')

    with open(csv_path, 'rb') as file:
        csv_data = file.read()
        file_storage = FileStorage(stream=io.BytesIO(csv_data), filename='departments.csv')

    with client.application.app_context():
        with mock.patch('controllers.charge_data_controller.ChargeDataController') as mock_request:
            mock_request.form.get.return_value = table_name
            mock_request.files.getlist.return_value = [file_storage]
            
            response = controller.handle_charge(mock_request)

    assert response.status_code == 200
    assert response.json == {'message': "Datos cargados con éxito."}

def test_charge_data_route_upload_failed(client: FlaskClient, mock_database):
    controller = ChargeDataController(mock_database)

    table_name = 'departments'
    csv_path = os.path.abspath('./test/resources/departments.csv')

    with open(csv_path, 'rb') as file:
        csv_data = file.read()
        file_storage = FileStorage(stream=io.BytesIO(csv_data), filename='departments.csv')

    with client.application.app_context():
        with mock.patch('controllers.charge_data_controller.ChargeDataController') as mock_request:
            mock_request.form.get.return_value = table_name
            mock_request.files.getlist.return_value = None
            
            response, status_code = controller.handle_charge(mock_request)

    assert status_code == 400
    assert response.json == {'error': 'No se han enviado archivos CSV'}
