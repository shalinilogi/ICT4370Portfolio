from datetime import datetime

class Stock:
	def __init__(self,symbol,shareQuantity):
		self.symbol=symbol
		self.shareQuantity=shareQuantity
		self.purchaseDate=[]
		self.openPrice=[]
		self.highPrice=[]
		self.lowPrice=[]
		self.closePrice=[]
		self.volume=[]
		self.stockValue=[]
		
		
	def add_DatePriceVolume(self,purchaseDate,openPrice,highPrice,lowPrice,closePrice,volume):
		self.purchaseDate.append(purchaseDate)
		if openPrice=='-':
			self.openPrice.append(0.00)
		else:
			self.openPrice.append(openPrice)
			
		if highPrice=='-':
			self.highPrice.append(0.00)
		else:
			self.highPrice.append(highPrice)
			
		if lowPrice=='-':
			self.lowPrice.append(0.00)
		else:
			self.lowPrice.append(lowPrice)
		self.closePrice.append(closePrice)
		self.volume.append(volume)
		self.stockValue.append(round(self.shareQuantity*closePrice,2))
		
	def add_GraphData(self,purchaseDates):
		stockValueGraph=[]
		for purchase in purchaseDates:
			if purchase in self.purchaseDate:
				index=self.purchaseDate.index(purchase)
				stockValueGraph.append(self.stockValue[index])
			else:
				stockValueGraph.append(None)
		return stockValueGraph
