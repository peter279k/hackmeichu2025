from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_calculate_electric_carbon_emission():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    json_dict = {
        'activity_data': 1000.0,
        'carbon_factor': 0.492,
    }

    response = client.post('/api/v1/calculate_electric', headers=headers, json=json_dict)

    response_json = response.json()

    assert response.status_code == 200
    assert response_json['data'] == 0.49
