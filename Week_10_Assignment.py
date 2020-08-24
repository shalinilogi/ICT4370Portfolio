"""
Author: Shalini Logidasan
Date: 8/8/2020
Function: The programe does the below

1. Displays an User Interface for the user to select the JSON file.

2. The JSON file path is used to read the data from the JSON file and store in the respective stock object

3. Stores the Investor and Stock Info in SQLite database.

4. Read the Stock Class files and stores the data in Pandas Data Frame

5. Plots the data from the Data Frame
"""


#Import libraries required to run the program
from tkinter import *
from tkinter import filedialog
from GUI import gui
import json
from StockW10 import*
import createTable
import matplotlib.pyplot as plt 
import pandas as pd


"""
Display User Interface (UI) to select the JSON file. The UI will have option to Select the file, Confirm the selection
and to quit the application
"""

root = Tk() #Variable for the root of the window

userInput=gui(root) #Variable to get the file path of the JSON

filePath=userInput.fileName

"""
From the file path stored in variable userInput read Stock information from the JSON file 
into a dictionary
"""

stockInfo ={} #Dictionary to store Stock information read from JSON file

stockQuantity={'GOOG':125,'AIG':235,'F':85,'FB':150,'IBM':80,'M':425,'MSFT':85,'RDS-A':400} # Assign the stock quantity

purchaseDates=[] #List to capture the Years we have Stock Data for all the stocks. This will be displayed in the X Axis

# Read the JSON file and store the information for each Stock in a dictionary

try:
	with open (filePath) as json_file:
		stock_data = json.load(json_file)
		for stock in stock_data:
			if stock['Symbol'] not in stockInfo:
				addStock=Stock(stock['Symbol'],stockQuantity[stock['Symbol']])
				addStock.add_DatePriceVolume(datetime.strptime(stock['Date'],"%d-%b-%y"),stock['Open'],stock['High'],stock['Low'],stock['Close'],stock['Volume'])
				stockInfo[stock['Symbol']]=addStock
				if datetime.strptime(stock['Date'],"%d-%b-%y") not in purchaseDates:
					purchaseDates.append(datetime.strptime(stock['Date'],"%d-%b-%y"))
			else:
				addStock.add_DatePriceVolume(datetime.strptime(stock['Date'],"%d-%b-%y"),stock['Open'],stock['High'],stock['Low'],stock['Close'],stock['Volume'])
				stockInfo[stock['Symbol']]=addStock
				if datetime.strptime(stock['Date'],"%d-%b-%y") not in purchaseDates:
					purchaseDates.append(datetime.strptime(stock['Date'],"%d-%b-%y"))
except Exception as ex:
	print('Exception was encoutered '+ex)
	sys.exit(1)

purchaseDates.sort() #Sort Dates in the list in ascending order

"""
Store the data read from the JSON file into SQLite database. Tables will be created for Investor and Stock Information
"""

#Initalize Database Connection

db="stockSummary.db"

cursor=createTable.createConnection(db)

#Create Investor, Stocks and Bonds table

createTable.createTable(cursor)

#Insert Investor information into the table

createTable.insertInvestor(cursor,301,'Bob Smith','5478 Colorado Blvd','303-876-5645')

cursor.commit()

#Insert Stock information into the table

purID=201 #set the Purchase ID to start from 201

try:
	for stock in stockInfo:
		symbol=stockInfo[stock].symbol
		#Inset stock Information into the database.
		for purDate in stockInfo[stock].purchaseDate:
			index=stockInfo[stock].purchaseDate.index(purDate)
			createTable.insertStocks(cursor,str(purID),symbol,str(purDate),str(stockQuantity[symbol]),str(stockInfo[stock].openPrice[index]),str(stockInfo[stock].highPrice[index]),str(stockInfo[stock].lowPrice[index]),str(stockInfo[stock].closePrice[index]),str(stockInfo[stock].volume[index]),301)
			purID=purID+1
except Exception as ex:
	print('Exception was encoutered '+ex)

cursor.commit() #Commit to the database

"""
Load the data stored in the dictionary to Pandas DataFrame
"""

df = pd.DataFrame(columns = ['Symbol','PurchaseDate','Quantity','OpenPrice','HighPrice','LowPrice','ClosePrice','Volume']) 

print("Data Load into Pandas in progress.Please wait")

try:
	for stock in stockInfo:
		symbol=stockInfo[stock].symbol
		#Inset stock Information into the database.
		for purDate in stockInfo[stock].purchaseDate:
			index=stockInfo[stock].purchaseDate.index(purDate)
			ls=[symbol,purDate,stockQuantity[symbol],stockInfo[stock].openPrice[index],stockInfo[stock].highPrice[index],stockInfo[stock].lowPrice[index],stockInfo[stock].closePrice[index],stockInfo[stock].volume[index]]
			df = df.append(pd.Series(ls,index = ['Symbol','PurchaseDate','Quantity','OpenPrice','HighPrice','LowPrice','ClosePrice','Volume']),ignore_index=True)
			
except Exception as ex:
	print('Exception was encoutered '+ex)
	
#print(df)
	
#Calculate the Average Stock Price for each stock 

Average=df[['OpenPrice','HighPrice','LowPrice','ClosePrice']].groupby(df['Symbol']).mean()

print("Average Stock price for each stock")

print(Average)

#Calculate the Standard Deviation for each stock 

standradDeviation=df[['OpenPrice','HighPrice','LowPrice','ClosePrice']].groupby(df['Symbol']).std()

print("Standard Deviation for each stock")

print(standradDeviation)
#Plot the Line diagram showing stock prices for each of the shares including the SPY for the time period.
fig,ax = plt.subplots(figsize=(18,6))

try:
	for name, group in df.groupby('Symbol'):
		group.plot(x='PurchaseDate', y='ClosePrice', ax=ax, label=name)
except Exception as ex:
	print('Exception was encoutered '+ex)

#Plot the Line Diagram
plt.show()


