
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

from ibapi.order import Order
from ibapi.order_state import OrderState


class BuyShares(EWrapper, EClient):
	def __init__(self):
		EWrapper.__init__(self)
		EClient.__init__(self, wrapper=self)
		self.nextValidOrderId = None
		self.contract = Contract()
		self.data = [] #Init variable to store candle ?
	
	def SendOrder(self, action):
		self.contract.symbol = sys.argv[2] #1 is 4002, 2 is sec name
		self.contract.secType = 'STK'
		self.contract.exchange = 'GLOBEX'
		self.contract.currency = 'USD'

		order = Order()
		order.action = action;
		order.totalQuantity = 1	#change it to command line argument
		order.orderType = 'MKT'
		self.placeOrder(self.nextOrderId(), self.contract, order)


def main():
	app = BuyShares()
	app.connect('127.0.0.1', port = 4002, clientId=108)
	print("serverVersion:%s connectionTime:%s" % (app.serverVersion(),app.twsConnectionTime()))
	app.run()
		
