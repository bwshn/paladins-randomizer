import re

with open('heros.txt', encoding="utf-8-sig") as f:
    lines = f.readlines()

classes = [re.sub("=.*", "", x).strip() for x in lines]

characters = []
for line in lines:
    characters += re.sub('[\[\]\,\"]', "", re.split("=", line)[1].strip()).split()

