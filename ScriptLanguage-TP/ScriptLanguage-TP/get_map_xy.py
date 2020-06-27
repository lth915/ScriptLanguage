import requests
import json

ApiKey = "2EA5653A-003C-3EC5-9B6C-02D8A98D5E40"

with open('정왕동맛집.json') as rstr:
    data = json.load(rstr)

for i in data:
    Address = i['roadAddress']
    r = requests.get('http://apis.vworld.kr/new2coord.do?q=' + 
                     Address + '&apiKey=' + ApiKey + 
                     '&domain=http://map.vworld.kr/&output=json')
    a = r.json()
    i['mapx'] = a['EPSG_4326_X']
    i['mapy'] = a['EPSG_4326_Y']

file = open("정왕동맛집.json", "w+")
file.write(json.dumps(data))  # 파일에 변경 내용 저장
