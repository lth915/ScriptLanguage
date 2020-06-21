
import json
from pprint import pprint

with open('정왕동맛집.json', encoding="utf-8") as rstr:
    data = json.load(rstr)

pprint(data)