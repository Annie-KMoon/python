#이미지 검색(카카오)
import requests
import os

def getData(query):
    url=f'https://dapi.kakao.com/v2/search/image?query={query}&size=20'
    headers={'Authorization':'KakaoAK 3b1f91160f090c6816a03b93720659b4'}
    res=requests.get(url, headers=headers)
    data = res.json()['documents']
    return data

if __name__=='__main__':
    query='아이유'
    list = getData(query)
    for item in list:
        image_url=item['image_url']
        res= requests.get(image_url)
        # print(res)

        if res.status_code==200:
            index=image_url.rindex('/')
            file_name=image_url[index+1:]
            #파일다운로드
            with open(f'data/image/{file_name}', 'wb') as file:
                file.write(res.content)