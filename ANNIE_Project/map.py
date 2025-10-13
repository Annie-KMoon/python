#삭제할 파일#

import pandas as pd
import json
import os
import folium


def getAddress():
    df = pd.read_csv('data/서울시 동물병원 인허가 정보.csv', encoding='ANSI')
    list = df[['관리번호','사업장명','도로명주소','상세영업상태명','좌표정보(X)','좌표정보(Y)']]
    return list

def searchAddress(address):
    list = getAddress()
    search_list = []
    for vet in list:
        if vet['address'].find(address)!=-1:
            print(f"{vet["사업장명"]}, {vet["상세영업상태명"]}, {vet["도로명주소"]}")
            search_list.append(vet)
    return search_list

def createMap(list, address):
    y =list[0]['좌표정보(Y)']
    x =list[0]['좌표정보(X)']
    location=(y, x)
    map = folium.Map(location, zoom_start=15, width='100%', height='100%')
    for store in list:
        location=(store['y'], store['x'])
        text = f'{store["name"]}<br>{store["phone"]}<br>{store["address"]}'
        popup=folium.Popup(text, max_width=200)
        folium.Marker(
            location,
            popup,
            icon=folium.Icon(color='blue', icon='glyphicon-road')
        ).add_to(map)

    map.save(f'data/map/{address}.html')

if __name__=='__main__':
    getAddress()

#     createMap(df2, address)
#     while True:        
#         print()
#         address = input("병원주소>")
#         if address=='':break
#         search_list=searchAddress(address)
#         if len(search_list)==0:
#             print('검색한 병원이 없습니다.')
#         else:
#             sel=input('지도를 출력하실래요(Y)>')
#             if sel=='Y' or sel=='y':
#                 createMap(search_list, address)