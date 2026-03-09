import requests
import pytest

URL = "http://localhost:8000"

def test_main():
    response = requests.get(f"{URL}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Pruebas unitarias"}

def test_suma():
    params = {
        "numero1": 10,
        "numero2": 5
    }
    response = requests.post(f"{URL}/sumas", params=params)
    assert response.status_code == 200
    assert response.json() == {"numero1": 10, "numero2": 5, "suma": 15}



