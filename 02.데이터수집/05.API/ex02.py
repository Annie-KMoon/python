#할리스 서울 매장정보
import json
import os
import requests

def getAddress():
    with open('data/hollys.json', 'r',encoding='utf-8')as file:
        address = json.load(file)
        # print(address) #파일 로드 확인
        list = []
        for add in address:
            data={'name':add['name'], 'address':add['address'], 'phone':add['phone']}
            list.append(data)
        return list  

# query='전북 삼성동 100'
# url=f'https://dapi.kakao.com/v2/local/search/address.json?query={query}'
# headers = {'Authorization': 'KakaoAK 3b1f91160f090c6816a03b93720659b4'}
# res =requests.request(method='get', url=url, headers=headers)
# print(res)

#주소 입력 위도(y), 경도(x) 
def getXY(query):
    url=f'https://dapi.kakao.com/v2/local/search/address.json?query={query}'
    headers={'Authorization':'KakaoAK 3b1f91160f090c6816a03b93720659b4'}
    res = requests.request(method='get', url=url, headers=headers)
    data = res.json()
    documents = data['documents']
    x = documents[0]['x']
    y = documents[0]['y']
    return x, y

if __name__=='__main__':
    list=getAddress()
    list_json = []
    for add in list:
        name = add['name']
        phone= add['phone']
        address=add['address']
        address = address.split(' ')[:4]
        address = ' '.join(address)
        xy = getXY(address)
        x = xy[0]
        y = xy[1]
        #print(address, x, y, name, phone)
        data={'name':name,'phone':phone,'address':address,'x':x,'y':y}
        list_json.append(data)

    with open('data/hollys_location.json', 'w', encoding='utf-8') as file:
        json.dump(list_json, file, indent='\t', ensure_ascii=False)    
    