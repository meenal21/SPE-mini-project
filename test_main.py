from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# we are creating a test case for every if scenario and an else scenario

def test_square_root():
    response = client.get("/sqrt?x=25")
    assert response.status_code == 200
    assert response.json() == {"result":5.0}

def test_square_root_negative():
    response = client.get("/sqrt?x=-25")
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot take square root of a negative number"

def test_factorial():
    response = client.get("/factorial?x=5")
    assert response.status_code == 200
    assert response.json() == {"result":120}

def test_factorial_negative():
    response = client.get("/factorial?x=-5")
    assert response.status_code == 400
    assert response.json()["detail"] == "Factorial not defined for negative numbers"

def test_natural_log():
    response = client.get("/ln?x=2.718")
    assert response.status_code == 200
    assert .999 < response.json()["result"] < 1.001

def test_natural_log_zero():
    response = client.get("/ln?x=0")
    assert response.status_code == 400
    assert response.json()["detail"] == "Natural log not defined for non-positive values"

def test_power():
    response = client.get("/power?x=5&b=2")
    assert response.status_code == 200
    assert response.json() == {"result":25.0}