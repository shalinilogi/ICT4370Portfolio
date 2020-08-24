"""
Author: Shalini Logidasan

Function: Create Database tables for Investor, Stock and Bond

Date: 7/31/20
"""

import sqlite3

def createConnection(dbFile):
	
	cursor = None
	
	try:
		cursor = sqlite3.connect(dbFile)
		return cursor
		
	except Exception as connEx:
		print('Exception was encoutered '+connEx)
		sys.exit(1)
		
		
def createTable(cursor):
	
	
	sql_create_investor_table = """ CREATE TABLE IF NOT EXISTS Investor (
										Investor_ID integer PRIMARY KEY,
                                        Name text NOT NULL,
                                        Address text NOT NULL,
                                        Phone_Number text Not Null
                                        ); """                                    
	
	sql_create_stock_table = """ CREATE TABLE IF NOT EXISTS Stocks (
                                        Purchase_ID integer PRIMARY KEY,
                                        Symbol text NOT NULL,
                                        Purchase_Date text NOT NULL,
                                        Shares_Quantity integer NOT NULL,
                                        Open_Price float Not NULL,
                                        High_Price float Not NULL,
                                        Low_Price float Not NULL,
                                        close_Price float Not NULL,
                                        Volume integer NOT NULL,
                                        Investor_ID integer NOT NULL
                                        ); """
                                                                    
	try:
		cursor.execute(sql_create_investor_table)
		cursor.execute(sql_create_stock_table)
	except Exception as ex:
		print('Exception was encoutered '+ex)
	
def insertInvestor(cursor,invID,invName,invAddress,invPhone):
	
	sql_insert= "INSERT INTO Investor VALUES("+str(invID)
	sql_insert= sql_insert+",'"+invName+"','"+invAddress+"','"+invPhone+"');"
	
	print(sql_insert)
	
	try:
		cursor.execute(sql_insert)
	except Exception as ex:
		print('Exception was encoutered '+ex)

def insertStocks(cursor,purID,stockName,purDate,stockQuantity,openPrice,highPrice,lowPrice,closePrice,volume,invID):
	
	sql_insert="INSERT INTO Stocks VALUES("+purID+",'"+stockName+"','"+purDate+"',"+stockQuantity+","+openPrice+","+highPrice+","+lowPrice+","+closePrice+","+volume+",'"+str(invID)+"');"
	
	print(sql_insert)
	
	try:
		cursor.execute(sql_insert)
	except Exception as ex:
		print('Exception was encoutered '+ex)
