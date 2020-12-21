import requests
from time import sleep

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

def test_car_add_functionality():
	response = requests.post(f'{BASE_URL}cars', json={"name": "toyota", "model": "x4", "doors": 5}, headers={"Content-Type":"application/json"})
	assert response.status_code == 200

def test_car_presence_functionality():
	response = requests.get(f'{BASE_URL}cars')
	present = False
	if response.status_code == 200:
		for car in response.json()["cars"]:
			if car["name"] == "toyota" and car["model"] == "x4" and car["doors"] == 5:
				present = True
	assert present

def test_car_delete_functionality():
	response = requests.get(f'{BASE_URL}cars')
	if response.status_code == 200:
		for car in response.json()["cars"]:
			if car["name"] == "toyota" and car["model"] == "x4" and car["doors"] == 5:
				id = car["id"]
				response = requests.delete(f'{BASE_URL}cars/{id}')
				if response.status_code != 200:
					assert False
				else:
					resp = requests.get(f'{BASE_URL}cars/{id}')
					assert resp.status_code == 404
