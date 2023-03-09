import re
from bs4 import BeautifulSoup
import requests

with open('heros.txt', encoding="utf-8-sig") as f:
    lines = f.readlines()

classes = [re.sub("=.*", "", x).strip() for x in lines]

characters = []
for line in lines:
    characters += re.sub('[\[\]\,\"]', "", re.split("=", line)[1].strip()).split()

urls = ["https://paladins.fandom.com/wiki/" + character for character in characters]

result = requests.get(urls[0])
doc = BeautifulSoup(result.text, "html.parser")

# TODO: keep the scraping for the talents.