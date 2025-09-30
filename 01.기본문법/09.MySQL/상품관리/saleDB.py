#매출관리 DB
from DB import*
from classes import*

def sale_list(value): #목록, 검색
    try:
        sql = 'select * from view_sale where code like %s or name like %s'
        value = f'%{value}%'
        cur.execute(sql,(value, value,))     
        rows = cur.fetchall()
        if rows!=None:
            sales=[]
            for row in rows:
                sale = Sale()
                sale.seq = row['seq']
                sale.code = row['code']
                sale.name = row['name']
                sale.price = row['price'] #판매가
                sale.qnt = row['qnt']
                sale.date= row['fdate']
                sale.sum = row['qnt']*row['price']
                sales.append(sale)
            return sales

    except Exception as err:
        print("매출목록오류:",err)

#매출등록
def sale_insert(sale):
    try:
        sql = 'insert into sale(code, date, qnt, price) values(%s,now(),%s,%s)'
        cur.execute(sql, (sale.code, sale.qnt, sale.price,))
        con.commit()
        print("매출등록성공!")
    except Exception as err:
        print("매출등록오류:",err)

#테스트
if __name__=="__main__":
    # pass

    #매출목록
    sales = sale_list("")
    for sale in sales:
        sale.print()