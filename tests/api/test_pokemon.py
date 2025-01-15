import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "bca00f9e9236f7cb39fea74ba44b4228"
HEADER =  {"Content-Type": "application/json" , "trainer_token": TOKEN}
TRAINER_ID = "12691"
TRAINER_NAME = "Sasha"


# Проверка статус кода в ответе на запрос GET /trainers = 200 
def test_status_code():
    response = requests.get(url = f"{URL}/trainers" , params = {"trainer_id": TRAINER_ID} )
    assert response.status_code == 200


# Проверка получения имени тренера в ответе
def test_trainer_name():
    response_get = requests.get(url = f"{URL}/me" , headers = HEADER, params = {"trainer_name": TRAINER_NAME} )
    assert response_get.json()["data"][0]["trainer_name"] == "Sasha"

