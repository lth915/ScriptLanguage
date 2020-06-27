import folium
import json

with open('정왕동맛집.json') as rstr:
    data = json.load(rstr)

m = folium.Map(
    location=[37,126], zoom_start=16
)   # 좌표값, 줌 확대 배율

folium.Marker(  # 마커추가하기
  location=[37,126],
  popup=data[0]['title'],
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

m.save('map.html')  # 파일로 저장