from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_get_electric_carbon_factor():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    json_dict = {
        'activity_data': 1000.0,
        'factor': 0.492,
    }

    response = client.post('/api/v1/electric_carbon_factor', headers=headers, json=json_dict)

    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json['data']['data']) > 0
