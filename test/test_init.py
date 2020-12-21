import requests

BASE_URL = "http://192.168.195.188:80/"

def test_base_status_code_equals_200():
     response = requests.get(BASE_URL)
     assert response.status_code == 200

def test_cars_status_code_equals_200():
     response = requests.get(f'{BASE_URL}cars')
     assert response.status_code == 200

def test_base_check_content_type_equals_json():
     response = requests.get(BASE_URL)
     assert response.headers["Content-Type"] == "application/json"

def test_cars_check_content_type_equals_json():
     response = requests.get(f'{BASE_URL}cars')
     assert response.headers["Content-Type"] == "application/json"
