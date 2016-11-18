#!/usr/bin/python

import os
import time
import json
import sys
import pyqrcode # pip install pyqrcode
import random



print("-----------------------------")
print("Python version : ")
print(sys.version)
print("Starting ......")
print("-----------------------------")
print("\n\n")

checkoutIdSave = 23482 # From DB




# Store Desc
storeName = "Machin Store"
storeAddress = "Quelque part ici"


# Checkout
checkoutMessage = "Bienvenue dans " + storeName

checkoutName = "Caisse 2"


checkoutTicketId  = 0
checkoutTotalAmount = 0



def getChckoutDate():
	return time.strftime("%d/%m/%Y")

def getCheckoutIdFromDB():
	global checkoutIdSave
	toReturn = checkoutIdSave
	checkoutIdSave += 1
	return toReturn

def printQRCode(data2Qr):
	#qrCode = pyqrcode.create(data2Qr, error='L')
	#qrCode1 = pyqrcode.create(data2Qr, error='M')
	#qrCode2 = pyqrcode.create(data2Qr, error='Q')
	qrCode3 = pyqrcode.create(data2Qr)
	#print(qrCode.terminal('green', 'white', quiet_zone=1))
	#qrCode.svg('qr.svg', scale=4, background = "white", module_color = "green")
	#qrCode1.svg('qr1.svg', scale=4, background = "white", module_color = "green")
	#qrCode2.svg('qr2.svg', scale=4, background = "white", module_color = "green")
	qrCode3.svg('qr3.svg', scale=4, background = "white", module_color = "green")



# Products
class Product:

	Produit = ""
	Prix = 0

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class ProductBasket:

	Produit = ""
	Prix = 0
	Qte = 0

	def __init__(self, product, qty):
		self.Produit = product.name
		self.Prix = product.price
		self.Qte = qty

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



class Customer:

	id = 0
	products = []
	qty = 0
	totalAmount = 0

	def __init__(self, id):
		self.id = id

	def addItem(self, product, qtyProduct):
		self.products.append( ProductBasket(product, qtyProduct) )
		self.qty += qtyProduct
		self.totalAmount += product.price * qtyProduct



	def getId(self):
		return self.id
	def getProducts(self):
		return self.products
	def getQty(self):
		return self.qty
	def getTotalAmount(self):
		return self.totalAmount


	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)




# Our soluce
class dematTicket:

	#{"Magasin": "Carrefour","Lieu": "Bordeaux","Caisse": "caisse 14","Date": "03/1/2016","Message": "Bienvenue","Produits": [{"Produit":"pain","Prix":2,"Qte":1},{"Produit":"lait","Prix":3,"Qte":1}],"Total": "5","NumeroTicket": "6306"}

	NumeroTicket = 0
	Magasin = ""
	Lieu = ""
	Caisse = ""
	Message = ""
	Date = ""
	Produits = []
	qty = 0
	Total = 0

	def __init__(self, storeName, storeAddress, checkoutName, checkoutMessage, customer):
		self.NumeroTicket = customer.getId()
		self.Magasin = storeName
		self.Lieu = storeAddress
		self.Caisse = checkoutName
		self.Message = checkoutMessage
		self.Date = time.strftime("%d/%m/%Y")

	def toJSON(self, customer):
		self.Produits = customer.getProducts()
		self.qty = customer.getQty()
		self.Total = customer.getTotalAmount()
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)




# Products
random.seed()

storeProductsList = [] # From DB
pomme = Product("Pomme", 0.3)
tomate = Product("Tomate", 0.2)
cookie = Product("Cookie", 1)
pain = Product("Pain", 0.90)
gateau = Product("Gateau", 15)
mouchoir = Product("Mouchoir", 4)
eau = Product("Eau", 0.10)
stylo = Product("Stylo", 0.1)
champagne = Product("Champagne", 50)



# Checkout ....
customer_14239538 = Customer(getCheckoutIdFromDB())
customer_14239538.addItem(product=pomme, qtyProduct=2)
customer_14239538.addItem(product=cookie, qtyProduct=5)
customer_14239538.addItem(product=gateau, qtyProduct=1)
customer_14239538.addItem(product=champagne, qtyProduct=2)
customer_14239538.addItem(product=tomate, qtyProduct=2)

# Add more item
#for x in range(0, 5):
#	customer_14239538.addItem(product=Product("item"+str(random.randrange(0, 100)), random.randrange(0, 100)), qtyProduct=random.randrange(1, 5))



ticket = dematTicket(storeName, storeAddress, checkoutName, checkoutMessage, customer_14239538)


print(customer_14239538.toJSON())
print('================================')
ticket2QrCodeData = ticket.toJSON(customer_14239538)
print( ticket2QrCodeData )
print('================================')
print( "len str : " + str(len(ticket2QrCodeData)))
print('================================')
printQRCode( ticket2QrCodeData )





