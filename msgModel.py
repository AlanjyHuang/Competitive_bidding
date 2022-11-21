#!C:\Users\HappyUser\AppData\Local\Programs\Python\Python38\python.exe
# -*- coding: utf-8 -*-
# 連線DB
from dbConfig import conn, cur


def getList():  # 取得所有商品屬性
    # 查詢
    sql = "select id, name, firstPrice, deadline, nowPrice from 上架 order by id;"
    cur.execute(sql)

    records = cur.fetchall()
    # return records
    ret = []

    for (id, name, firstPrice, deadline, nowPrice) in records:
        temp = {
            'id': id,
            'name': name,
            'firstPrice': firstPrice,
            'deadline': deadline,
            'nowPrice': nowPrice
        }
        # print(temp)
        ret.append(temp)

    return ret


def subscript(uid, product_id, price):  # 下標
	# 檢查下標價格
    checkSql = "select nowPrice from 上架 where id = %s"
    cur.execute(checkSql, ([product_id]))
    checkPrice = cur.fetchall()
    if (price < checkPrice[0]):
        return False
    else:
        sql = "insert into 下標 (UID, product_id, price) values (%s, %s, %s)"
        cur.execute(sql, (uid, product_id, price))
        conn.commit()
		# 更新最高價
        updateNowPriceSql = "update 上架 set nowPrice = %s where id = %s"
        cur.execute(updateNowPriceSql, (price, product_id))
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
            'time': time,
            'success': 成功
        }
        ret.append(temp)

    return ret


def addProduct(name, firstPrice, deadline): # 上架商品
    sql = "insert into 上架 (name, firstPrice, deadline, nowPrice) values %s, %s, %s, %s)"
    cur.execute(sql, (name, firstPrice, deadline, firstPrice))
    conn.commit()
    return True
