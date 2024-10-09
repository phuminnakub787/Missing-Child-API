import requests
from bs4 import BeautifulSoup
import json

url = "https://web.backtohome.org/missing%20children.php?width=1920&height=1080"
web_data = requests.get(url)

soup = BeautifulSoup(web_data.text,'html.parser')
find_word = soup.find_all("div",{"class":"miss_detail"})

miss_child = []
j=0

for i in find_word:
    j+=1

    img = i.find_previous("div",{"class":"miss_img"})
    img = img.find("img")
    img = img["src"] if img else None

    name = i.find_all("div",align="center")[0].text.strip()
    age = i.find_all("div",align="center")[1].text.strip()

    miss_child.append({
        "id":j,
        "name":name,
        "age":age,
        "img":img
    })

with open("miss_child.json","w",encoding = "utf-8") as json_file:
    json.dump(miss_child,json_file,ensure_ascii = False,indent = 4)