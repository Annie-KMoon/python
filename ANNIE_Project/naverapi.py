# 네이버 검색 API: 뉴스검색
import requests
import urllib.request
import json

#함수생성
def getNews(query, start, display):
    client_id = "DSISkunI4gxjpwj6Yl6J"
    client_secret = "CxLnF9_VmQ"
    encText = urllib.parse.quote(query)
    url = f"https://openapi.naver.com/v1/search/news.json?query={encText}&start={start}&display={display}" 
    # #+ encText # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query={encText}&start={start}&display={display}" # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        result = json.loads(result) #jsontype
        # print(response_body.decode('utf-8'))
        return result['items'], result['total']
    else:
        print("Error Code:" + rescode)
        return None
