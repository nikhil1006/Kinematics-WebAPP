import pytest
from app import app
from flask.testing import FlaskClient

def test_home():
    client = FlaskClient(app)
    response = client.get('/')
    assert response.status_code == 200
    assert b'Kinematics Calculator' in response.data

def test_submit_form():
    client = FlaskClient(app)

    # Sample input
    data = {
        "endpoints": "(0.7, 0.5) (-0.2, 0.8) (-0.9, -0.3) (0.3, -0.5) (1.0, 0.3) (0.2, 1.0) (-1.0, -0.2) (-0.2, -1.0) (0.7, 0.8) (-0.9, 0.7)"
    }

    # Submit the form
    response = client.post("/calculate", data=data)

    # Check if the response is successful (status code 200)
    assert response.status_code == 200

    # Check if the response contains some expected result
    # Replace 'Expected result string' with an appropriate string from your application's response
    #assert b'Expected result string' in response.data
