import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import pytest
from unittest import mock
from src.app import create_app
from flask import Flask
from flask.testing import FlaskClient

@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_database(mocker):
    mock_database = mocker.MagicMock()
    mock_session = mock.MagicMock()
    mock_database.get_session.return_value = mock_session
    mock_session.bulk_save_objects.side_effect = lambda batch: None  # Simular inserción exitosa
    mock_session.commit.side_effect = lambda: None  # Simular commit exitoso
    mock_session.close.side_effect = lambda: None  # Simular cierre de sesión exitoso
    
    yield mock_database
