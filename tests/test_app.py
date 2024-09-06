from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_aula.app import app

client = TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange
    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Asset
