from app.main import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_retrieve_electric_carbon_factor_data():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    response = client.get('/api/v1/electric_carbon_factor', headers=headers)

    response_json = response.json()

    assert len(response_json['data']['data']) > 0
