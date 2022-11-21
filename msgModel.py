from dbConfig import conn, cur

def getList(): # 取得商品屬性
	#查詢
	sql="select id, name, firstPrice, deadline, nowPrice from 上架 order by id;"
	cur.execute(sql)
	
	records = cur.fetchall()
	#return records
	ret=[]
	
	for (id, name, firstPrice, deadline, nowPrice) in records:
		temp={
			'id': id,
			'name': name,
			'firstPrice': firstPrice,
			'deadline': deadline,
			'nowPrice': nowPrice
		}
		#print(temp)
		ret.append(temp)
		
	return ret
	
def subscript(uid, product_id, price): #下標
	sql = "insert into 下標 (UID, pruduct_id, price) values (%s, %s, %s)"
	cur.execute(sql, (uid, product_id, price))
	conn.commit()
	return True

def subscriptHistory(uid):
	sql = "select id, product_id, price, time, 成功 from 下標 where UID = %s"
	cur.execute(sql, ([uid]))
	records = cur.fetchall()