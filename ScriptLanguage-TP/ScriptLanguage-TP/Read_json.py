
import json
from pprint import pprint

with open('정왕동맛집.json') as rstr:
    data = json.load(rstr)

pprint(data) 