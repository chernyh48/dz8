import requests

heroes = requests.get("https://akabab.github.io/superhero-api/api/all.json")
heroes_list = ["Hulk", "Captain America", "Thanos"]
heroes_id = {}
heroes_intelligence = {}
for i in heroes_list:
    for j in heroes.json():
        if j['name'] == i:
            heroes_id[i] = j["id"]
for i in heroes_id:
    hero_stat = requests.get(f"https://akabab.github.io/superhero-api/api/powerstats/{heroes_id[i]}.json")
    heroes_intelligence[i] = hero_stat.json()["intelligence"]
print(f"Самый умный из Hulk, Captain America, Thanos: {max(heroes_intelligence, key=heroes_intelligence.get)}")
