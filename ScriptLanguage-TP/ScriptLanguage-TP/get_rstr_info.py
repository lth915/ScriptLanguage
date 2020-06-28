import requests
import json
from urllib.parse import quote

# 네이버 api 부르기
def call(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/local?query=" + encText + "&display=10" + "&start=" + str(start)
    result = requests.get(url=url, headers={"X-Naver-Client-Id": "cf7S5Eg7pymBjoGjsSX_", "X-Naver-Client-Secret": "naor0GFc7m"})
    print(result)  # Response 성공시 [200] 출력
    return result.json()
 
# 검색 결과 가져오기
def getresults(keyword):
    list = []
    for num in range(0,10):
        list = list + call(keyword, num * 100 + 1)['items'] # json = items / xml = item
    return list

text = input("검색할 지역명을 입력하세요[ex) 정왕동, 배곧, ...]: ") 

list = []
result = getresults(text + '맛집')
list = list + result
 
file = open(text + "맛집.json", "w+")  # 검색 결과 json 파일로 저장
file.write(json.dumps(list))  # 파일에 쓰기