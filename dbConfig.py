#!C:\Users\HappyUser\AppData\Local\Programs\Python\Python38\python.exe
#-*- coding: utf-8 -*-

#import mariadb
import mysql.connector 

try:
 	#conn = mariadb.connect(
	conn = mysql.connector.connect(
		user="root",
		password="",
		host="127.0.0.1",
		port=3306,
		database="competitive_bidding"
	)
except: #mariadb.Error as e:
	print("Error connecting to DB")
	exit(1)

cur=conn.cursor() #use array to output query results
#cur = conn.cursor(dictionary=True) #use dict to output query results