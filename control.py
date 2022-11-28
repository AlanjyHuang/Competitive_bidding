#!C:\Users\Alanjy_Huang\AppData\Local\Programs\Python\Python38-32\python.exe
# -*- coding: utf-8 -*-

#print headers first
print("Content-Type: text/html; charset=utf-8\n")
#print("Content-type: application/json; charset: utf-8\n")
#print("HELLO")
import json
from datetime import date, datetime
import cgi
import msgModel

#main starts here
form = cgi.FieldStorage()
try:
	act=form.getvalue('o')
except:
	print("o missing")
	exit()

para=()
#we can start accessing DB now

if act=='getProductList': #get one record by xid
	#print("getProductlist")
	msgList = msgModel.getList() #get an array from model
	#print(msgList)
	result = {
		"list": msgList
	}
	#print(result)
	print(json.dumps(result,ensure_ascii=True)) #dump json string to client
elif act=='getHistory': #get one record by xid
	#print("getProductlist")
	msgList = msgModel.getHistory() #get an array from model
	#print(msgList)
	result = {
		"list": msgList
	}
	#print(result)
	print(json.dumps(result,ensure_ascii=True)) #dump json string to client
elif act=='subscript':
	uid=form.getvalue('uid')
	product_id=form.getvalue('product_id')
	price=form.getvalue('price')
	#print(uid,product_id,price)
	ret=msgModel.subscript(uid,product_id,price)
	#print("ret:",ret)
	if ret:
		print("success to subscript")
	else:
		print("the subscript time has pass, fail to subscript")
elif act=="getHistoryUID":
#	print("in control")
	jsonStr=form.getvalue('UID')
#	print(jsonStr)
	msgList = msgModel.subscriptHistory(jsonStr) 
	# print(msgList)
	result = {
			"list": msgList
		}
	#print(result)
	print(json.dumps(result,ensure_ascii=True)) #dump json string to client
elif act=="addProductInList":
	name=form.getvalue('name')
	firstPrice=form.getvalue('firstPrice')
	deadline=form.getvalue('deadline')
	data = msgModel.addProduct(name,firstPrice,deadline)
	print(data)
