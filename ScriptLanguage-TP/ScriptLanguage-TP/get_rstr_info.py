import requests
import json
from urllib.parse import quote

# 네이버 api 부르기
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/local?query=" + encText + "&display=10" + "&start=" + str(start)
    result = requests.get(url=url, headers={"X-Naver-Client-Id": "cf7S5Eg7pymBjoGjsSX_", "X-Naver-Client-Secret": "naor0GFc7m"})
    print(result)  # Response [200]
    return result.json()
 
# 검색 결과 받아오기
def getresults(keyword):
    list = []
    for num in range(0,10):
        list = list + call(keyword, num * 100 + 1)['items'] # list 안에 키값이 item 인 애들만 넣기
    return list

list = []
result = getresults("정왕동 맛집")
list = list + result
 
file = open("정왕동맛집.json", "w+")  # gangnam.json 파일을 쓰기 가능한 상태로 열기 (만들기)
file.write(json.dumps(list))  # 쓰기
 