import folium

m = folium.Map(
    location=[37.340532,126.733561], zoom_start=16
)   # 좌표값, 줌 확대 배율

folium.Marker(  # 마커추가하기
  location=[37.340532,126.733561],
  popup='한국산업기술대',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

m.save('map.html')  # 파일로 저장