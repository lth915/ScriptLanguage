import json
import numpy
import folium
from pyproj import Proj, transform
from pprint import pprint

with open('정왕동맛집.json') as rstr:
    data = json.load(rstr)

# UTM-K
proj_UTMK = Proj(init='epsg:5178') # UTM-K 변환
# WGS1984
proj_WGS84 = Proj(init='epsg:4326') # Wgs84 경도/위도 변환

for i in data:
    i['mapx'], i['mapy'] = transform(proj_UTMK,proj_WGS84,i['mapx'],i['mapy'])
    print(i['mapx'])
    print(i['mapy'])

#file = open("정왕동맛집.json", "w+")
#file.write(json.dumps(data))  # 파일에 변경 내용 저장