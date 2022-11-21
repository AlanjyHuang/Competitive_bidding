#!C:\Users\HappyUser\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf-8 -*-

#print headers first
print("Content-Type: text/html; charset=utf-8\n")
#print("Content-type: application/json; charset: utf-8\n")

import json
from datetime import date, datetime
import cgi
import msgModel

#main starts here
form = cgi.FieldStorage()
try:
	act=form.getvalue('o') #取得命令
except:
	# print("o missing")
	exit()

para=()

if act=='getProductList': # 取得貨品資料
	msgList = msgModel.getList() #呼叫getlist 取得DB裡的貨品資廖
	result = {
		"list": msgList
	}
	print(json.dumps(result,ensure_ascii=True)) #回傳給主畫面
elif act=='subscript': #下標
	jsonStr=form.getvalue('body') #將主畫面的參數取出
	ret=msgModel.subscript(jsonStr['uid'],jsonStr['product_uid'],jsonStr['price'])
	#將參數轉送給msgmodel 進行資料庫的下標
	if ret:
		print("success to subscript")
	else:
		print("the subscript time has pass, fail to subscript")
elif act=="subscriptHistory":  #列出下標歷史
	jsonStr=form.getvalue('body')
	dat=json.loads(jsonStr)
	msgList = msgModel.subscriptHistory(jsonStr['uid']) #呼叫msgmodel查詢
	result = {
		"list": msgList
	}
	#回傳下標
	print(json.dumps(result,ensure_ascii=True)) #dump json string to client
elif act=="addProductInList":
	#上架商品
	name=form.getvalue('name')
	firstPrice=form.getvalue('firstPrice')
	deadline=form.getvalue('deadline')
	data = msgModel.addProduct(name,firstPrice,deadline)
 #呼叫msgModel.addProduct新增資料庫
	print(data)
	