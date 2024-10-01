import requests
import pytest


@pytest.fixture()
def obj_id():
    payload = {
        "email": "Dallaso@mail.com",
        "password": "asdfg",
    }
    response = requests.post("http://127.0.0.1:8000/v1/users", json=payload).json()
    yield response["id"]
    requests.delete(f"http://127.0.0.1:8000/v1/users/{response["id"]}")


def test_create_object(obj_id):
    payload = {
        "email": "Jumbo@mail.com",
        "password": "zxcv",
    } 
    response = requests.post("http://127.0.0.1:8000/v1/users", json=payload).json()
    assert response["email"] == payload["email"]
    requests.delete(f"http://127.0.0.1:8000/v1/users/{response["id"]}")


def test_get_list_of_users():
    url = "http://127.0.0.1:8000/v1/users"
    response = requests.get(url)
    assert response.status_code == 200


def test_get_object(obj_id):
    # print(obj_id)
    response = requests.get(f"http://127.0.0.1:8000/v1/users/{obj_id}").json()
    assert response["id"] == obj_id
