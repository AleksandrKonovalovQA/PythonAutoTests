import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "bca00f9e9236f7cb39fea74ba44b4228"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN}

# Создаем Покемона
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.status_code)
print(response_create.text)

# Извлекаем pokemon_id из ответа
response_data_create = response_create.json()
pokemon_id = response_data_create.get("id")  # Проверяем наличие поля "id"
if pokemon_id:
    print(f"Создан Pokémon с ID: {pokemon_id}")
else:
    print("Не удалось получить ID покемона")
    exit()  # Прекращаем выполнение, если ID не найден

# Изменяем имя и фото Покемона
body_rename = {
    "pokemon_id": pokemon_id,
    "name": "Чаризард",
    "photo_id": 2
}

response_rename = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_rename)
print(response_rename.status_code)
print(response_rename.text)

# Поймать Покемона
body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_catch)
print(response_catch.status_code)
print(response_catch.text)

# Удалить Покемона
body_knockout = {
    "pokemon_id": pokemon_id
}

response_knockout = requests.post(url=f'{URL}/pokemons/knockout', headers=HEADER, json=body_knockout)
print(response_knockout.status_code)
print(response_knockout.text)
