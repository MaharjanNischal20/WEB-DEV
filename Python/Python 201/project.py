import requests

while True:
    characterName = input("Which character you wanna pick, huh?? ")
    characterName = characterName.lower()

    if characterName == "gg":
        break

    req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{characterName}')

    if req.status_code == 200:
        character = req.json()

        print("Name is\t\t",character['name'])
        print("Abilities are:")
        for ability in character['abilities']:
            print(ability['ability']['name'])

    else:
        print("Pokemon's Character not found!!")
