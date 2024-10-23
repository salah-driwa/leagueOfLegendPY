# -*- coding: utf-8 -*-
"""League of legends WS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Npo6pYn5nv8QGNUO7c45h6juOuBAnw1S
"""

import requests
from bs4 import BeautifulSoup
import json
from google.colab import files  # Import files module for downloading

# Full list of champions
champions = [
    "Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie",
    "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard", "Bel'Veth", "Blitzcrank",
    "Brand", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
    "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn",
    "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen",
    "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi",
    "Irelia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx",
    "Kai'Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle",
    "Kayn", "Kennen", "Kha'Zix", "Kindred", "Kled", "Kog'Maw", "K'Sante",
    "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu",
    "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Milio",
    "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
    "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu & Willump", "Olaf",
    "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan",
    "Rammus", "Rek'Sai", "Rell", "Renata Glasc", "Renekton", "Rengar",
    "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine",
    "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner",
    "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Taliyah",
    "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere",
    "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar",
    "Vel'Koz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear",
    "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone",
    "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"
]

# Base URL
base_url = "https://www.leagueoflegends.com/en-au/champions/"

# Initialize a list to hold all champions' data
all_champions_data = []

# Iterate over each champion
for champion in champions:
    champion_url = f"{base_url}{champion.lower().replace(' ', '')}/"
    response = requests.get(champion_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant data
        name = soup.find(class_='sc-5201b421-0 dxZqcd').text
        subname = soup.find(class_='sc-f995a07a-0 dstnll').text
        description = soup.find(class_='sc-4225abdc-0 lnNUuw').text
        meta_details = soup.find_all(class_='meta-details')
        role = meta_details[0].text
        difficulty = meta_details[1].text

        # Find abilities
        abilities_container = soup.find_all(class_='sc-d7ac92a-0 dTVXdJ horizontal')[0]
        abilities = abilities_container.find_all('li')

        champ_abilities = []
        for ability in abilities:
            ability_name = ability.find('div', class_='icon-tab-label').text
            ability_img = ability.find('img')['src']
            champ_abilities.append({'name': ability_name, 'image': ability_img})

        # Find skins
        skins_container = soup.find_all(class_='sc-22590255-0 kbuMqN')[1]
        skins = skins_container.find_all('li')

        skin_data = []
        for skin in skins:
            skin_name = skin.find(class_='sc-76b4d5e-1 dpFoPT').text
            skin_img = skin.find('img')['src']
            skin_data.append({'name': skin_name, 'image': skin_img})

        # Group all data for the champion
        champion_data = {
            'name': name,
            'subname': subname,
            'description': description,
            'role': role,
            'difficulty': difficulty,
            'abilities': champ_abilities,
            'skins': skin_data
        }

        all_champions_data.append(champion_data)
    else:
        print(f"Failed to retrieve data for {champion}.")

# Export the data as JSON
json_file_path = 'champions_data.json'
with open(json_file_path, 'w') as json_file:
    json.dump(all_champions_data, json_file, indent=4)

# Download the JSON file
files.download(json_file_path)

print("Champions' data exported to champions_data.json and is now available for download.")