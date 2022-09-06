from datetime import datetime
import requests
import time

days = int(input("За сколько последних дней получить вопросы?\n"))
tagged = input("Введите тег для сортировки:\n").lower()

fromdate = round(time.time()) - (days * 86400)
params = {"page": 1, "pagesize": 100, "fromdate": fromdate, "order": "asc", "sort": "creation", "tagged": tagged,
          "site": "stackoverflow"}
result_dict = {}
while True:
    time.sleep(2)
    res = requests.get("https://api.stackexchange.com/2.3/questions", params=params)
    if res.json()['has_more'] is False:
        break
    for i in res.json()['items']:
        result_dict[datetime.utcfromtimestamp(i["creation_date"]).strftime('%Y-%m-%d %H:%M:%S')] = {"title": i["title"],
                                                                                                    "link": i["link"]}
    params["page"] += 1
n = 1
for i in result_dict:
    with open("result_task_3.txt", "a", encoding='utf-8') as f:
        f.write(f"№{n}\n{i}\n{result_dict[i]['title']}\n{result_dict[i]['link']}\n")
    n += 1
