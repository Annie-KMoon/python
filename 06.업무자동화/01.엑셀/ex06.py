#csv 파일 엑셀파일화
import csv
file = open('data/score.csv', 'r', encoding='utf-8')
read_file = csv.reader(file)
scores = []
for score in read_file:
    scores.append(score)


from openpyxl import Workbook
wb = Workbook()
ws = wb.active

for score in read_file:
    ws.append(tuple(score))

wb.save('data/score.xlsx')
wb.close()