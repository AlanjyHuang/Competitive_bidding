#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
# -*- coding: utf-8 -*-
# 連線DB
from dbConfig import conn, cur

def subscriptFinishHistory():
    # 查詢已結標商品
   # print("in getList")
    sql = "select id, name, firstPrice, deadline, nowPrice, getMan from `上架` where deadline < now() order by id;"
    cur.execute(sql)

    records = cur.fetchall()
    # return records
    ret = []
   # print(records)
    for (id, name, firstPrice, deadline, nowPrice, getMan) in records:
       # print(deadline.strftime('%Y-%m-%d %H:%M:%S'))
        temp = {
            'product_id': id,
            'name': name,
            'firstPrice': firstPrice,
            'deadline': deadline.strftime('%Y-%m-%d %H:%M:%S'),
            'nowPrice': nowPrice,
            'getMan': getMan
        }
       # print(temp)
        ret.append(temp)
    return ret


def getHistory(product_id2):  # 取得所有商品屬性
    # 查詢
    #print("pid",product_id2)
    #print("in getList")
    sql = "select product_id, UID, price, time from 下標 where product_id=%s order by time;"
    cur.execute(sql,([product_id2]))
    records = cur.fetchall()
    # return records
    ret = []
  #  print(records)
    for (product_id, UID, price, time) in records:
       # print(deadline.strftime('%Y-%m-%d %H:%M:%S'))
        temp = {
            'product_id': product_id,
            'UID': UID,
            'price': price,
            'time': time.strftime('%Y-%m-%d %H:%M:%S'),
        }
       # print(temp)
        ret.append(temp)
    #print(ret)
    return ret

def getList():  # 取得所有商品屬性
    # 查詢
   # print("in getList")
    sql = "select id, name, firstPrice, deadline, nowPrice,getMan from 上架 where now() < deadline order by id;"
    cur.execute(sql)

    records = cur.fetchall()
    # return records
    ret = []
   # print(records)
    for (id, name, firstPrice, deadline, nowPrice,getMan ) in records:
       # print(deadline.strftime('%Y-%m-%d %H:%M:%S'))
        temp = {
            'product_id': id,
            'name': name,
            'firstPrice': firstPrice,
            'deadline': deadline.strftime('%Y-%m-%d %H:%M:%S'),
            'nowPrice': nowPrice,
            'getMan':getMan 

        }
       # print(temp)
        ret.append(temp)
    #print(temp)
    return ret


def subscript(uid, product_id, price):  # 下標
	# 檢查下標價格
    checkSql = "select nowPrice from 上架 where id = %s"
    cur.execute(checkSql, ([product_id]))
    checkPrice = cur.fetchall()
    #print(checkPrice[0][0])
    if (int(price) < int(checkPrice[0][0])):
        #print("fail subscript")
        return False
    else:
      #  print("success subscript")
        sql = "insert into 下標 (UID, product_id, price) values (%s, %s, %s)"
        cur.execute(sql, (uid, product_id, price))
        conn.commit()
		# 更新最高價
        updateNowPriceSql = "update 上架 set nowPrice = %s where id = %s"
        cur.execute(updateNowPriceSql, (price, product_id))
        conn.commit()
        updateNowPriceSql = "update 上架 set getMan = %s where id = %s"
        cur.execute(updateNowPriceSql, (uid, product_id))
        conn.commit()
        return True


def subscriptHistory(uid): # 取得下標歷史
    sql = "select id, product_id, price, time, 成功 from 下標 where UID = %s"
    
    cur.execute(sql, ([uid]))
    records = cur.fetchall()

    ret = []

    for (id, product_id, price, time, 成功) in records:
        temp = {
            'id': id,
            'product_id': product_id,
            'price': price,
            'time': time.strftime('%Y-%m-%d %H:%M:%S'),
            'success': 成功
        }
        ret.append(temp)

    return ret


def addProduct(name, firstPrice, deadline): # 上架商品
    sql = "insert into 上架 (name, firstPrice, deadline, nowPrice) values (%s, %s, %s, %s)"
    cur.execute(sql, (name, firstPrice, deadline, firstPrice))
    conn.commit()
    return True
