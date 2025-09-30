import requests #네트워크접속
import os


#카카오 API를 활용한 다음 도서검색 gkatn
def getBooks(url, query, page, size):
    try:
        # "Authorization: KakaoAK ${REST_API_KEY}" 개인 API사용 헤더>>
        headers = {'Authorization': 'KakaoAK 3b1f91160f090c6816a03b93720659b4'}
        url = f"{url}?query={query}&page={page}&size={size}"
        res =requests.request(method='get', url=url, headers=headers)
        data = res.json()
        # print(data)
        documents = data['documents']
        # print(len(documents))
        if len(documents)==0:
            print("검색도서가 없습니다.")
        for idx, doc in enumerate(documents):
            title = doc['title']
            price = doc['price']
            sale_price = doc['sale_price']
            authors = doc['authors']
            authors =','.join(authors)
            publisher = doc['publisher']
            print(f'{idx+1}){title}|{authors}|{publisher}|{price:,}원')

    except Exception as err:
        print("접속오류:",err)



if __name__ =="__main__":
    # url = "https://dapi.kakao.com/v3/search/book" #접속URL
    # query = "파이썬" #검색어
    # page = 1 #페이지
    # size = 10 #10개씩
    # getBooks(url, query, page, size)


#도서검색 직접입력으로 수정
    url = "https://dapi.kakao.com/v3/search/book" #접속URL
    page = 1 #페이지
    size = 10 #10개씩

    os.system('cls')
    while True:
        query = input("검색도서명>")
        if query == "":
            input("검색을 종료합니다.")
            break
    
        getBooks(url, query, page, size)