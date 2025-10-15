from openpyxl import Workbook #Workbook-엑셀파일

wb = Workbook() #워크북객체생성
ws = wb.active #워크북내 시트 선택
ws.title = '나의시트' #타이틀 설정

wb.save('data/sample.xlsx') #저장
wb.close() #닫기
