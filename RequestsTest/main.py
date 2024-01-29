import requests

URL="https://api.pokemonbattle.me:9104"
header={"Content-Type": 'application/json', "trainer_token": "e275d0085bee245220ca730b1706cf70"}


# Запрос на создание покемонa                      
body={
    "name": "generate",
    "photo": "generate"
}

response=requests.post(url=f"{URL}/pokemons", json=body, headers=header, timeout=5)
print(f"Статус код:{response.status_code}. Сообщение: {response.text}")

# Запрос на изменение имени покемона
body1={
        "pokemon_id": "28957",
        "name": "SOVA",
        "photo": "https://dolnikov.ru/pokemons/albums/056.png"
}

response=requests.put(url=f"{URL}/pokemons", json=body1, headers=header, timeout=5)
print(f"Статус код:{response.status_code}. Сообщение: {response.text}")

# Запрос на добаление покемона в покебол
body2={
    "pokemon_id": "28957"
}
response=requests.post(url=f"{URL}/trainers/add_pokeball", json=body2, headers=header, timeout=5)
print(f"Статус код:{response.status_code}. Сообщение: {response.text}")