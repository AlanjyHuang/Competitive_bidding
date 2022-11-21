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
	act=form.getvalue('o')
except:
	# print("o missing")
	exit()

para=()
#we can start accessing DB now

if act=='getProductList': #get one record by xid
	msgList = msgModel.getList() #get an array from model
	result = {
		"list": msgList
	}
	print(json.dumps(result,ensure_ascii=True)) #dump json string to client
elif act=='subscript':
	jsonStr=form.getvalue('body')
	ret=msgModel(jsonStr['uid'],jsonStr['product_uid'],jsonStr['price'])
	if ret:
		print("success to subscript")
	else:
		print("the subscript time has pass, fail to subscript")
elif act=="subscriptHistory":
	jsonStr=form.getvalue('body')
	dat=json.loads(jsonStr)
	msgList = msgModel.subscriptHistory(jsonStr['uid']) 
	result = {
		"list": msgList
	}
	print(json.dumps(result,ensure_ascii=True)) #dump json string to client
elif act=="addProductInList":
	name=form.getvalue('name')
	firstPrice=form.getvalue('firstPrice')
	deadline=form.getvalue('deadline')
	data = msgModel.addProductInList(name,firstPrice,deadline)
	print(data)
