from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer
from datetime import datetime
import pendulum
#https://pendulum.eustace.io

port = 7497  # Simulated + TWS
#port = 4002 # Simulated + Gateway

#buy ES
class buyES(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.done = False
        self.nextOrderId = ""

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        self.start()

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print("OrderStatus. Id: ", orderId, ", Status: ", status, ", Filled:", filled, ", Remaining: ", remaining,
              ", LastFillPrice: ", lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print("OpenOrder. ID:", orderId, contract.symbol, contract.secType, "@", contract.exchange, ":", order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print("ExecDetails. ", reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


    def start(self):

        #define the contract
        contract = Contract()
        contract.symbol = "ES"
        contract.secType = "FUT"
        contract.exchange = "GLOBEX"
        contract.currency = "USD"
        contract.lastTradeDateOrContractMonth = "202109"

        #place the order
        order = Order()
        order.action = "BUY"   #"BUY"
        order.totalQuantity = 1
        order.orderType = "MKT"
        self.placeOrder(self.nextOrderId, contract, order)

    def stop(self):
        self.done = True
        self.disconnect()

class EScall(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.done = False
        self.nextOrderId = ""

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        self.start()

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print("OrderStatus. Id: ", orderId, ", Status: ", status, ", Filled:", filled, ", Remaining: ", remaining,
              ", LastFillPrice: ", lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print("OpenOrder. ID:", orderId, contract.symbol, contract.secType, "@", contract.exchange, ":", order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print("ExecDetails. ", reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


    def start(self):

        #define the contract
        contract = Contract()
        contract.symbol = "ES"
        contract.secType = "FOP"
        contract.exchange = "GLOBEX"
        contract.currency = "USD"
        contract.multiplier = "50"

        #place the order
        order = Order()
        order.action = action
        contract.right = putcall
        contract.strike = strike
        contract.lastTradeDateOrContractMonth = expr
        order.totalQuantity = 1
        order.orderType = "MKT"
        self.placeOrder(self.nextOrderId, contract, order)

    def stop(self):
        self.done = True
        self.disconnect()

class SellEScall(EWrapper, EClient):

    def __init__(self):
        EClient.__init__(self, self)
        self.done = False
        self.nextOrderId = ""

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def nextValidId(self, orderId):
        self.nextOrderId = orderId
        self.start()

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print("OrderStatus. Id: ", orderId, ", Status: ", status, ", Filled:", filled, ", Remaining: ", remaining,
              ", LastFillPrice: ", lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print("OpenOrder. ID:", orderId, contract.symbol, contract.secType, "@", contract.exchange, ":", order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print("ExecDetails. ", reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


    def start(self):

        #define the contract
        contract = Contract()
        contract.symbol = "ES"
        contract.secType = "FOP"
        contract.exchange = "GLOBEX"
        contract.currency = "USD"
        contract.multiplier = "50"

        #place the order
        order = Order()
        order.action = "sell"
        contract.right = "C"
        contract.strike = 4380
        contract.lastTradeDateOrContractMonth = "20210813"
        order.totalQuantity = 1
        order.orderType = "MKT"
        self.placeOrder(self.nextOrderId, contract, order)

    def stop(self):
        self.done = True
        self.disconnect()

#   nextMonday = pendulum.now().next(pendulum.MONDAY)
#   nextSunday = nextMonday.next(pendulum.SUNDAY)
#   nextMonday = nextMonday.strftime('%d/%m/%Y')
#   nextSunday = nextSunday.strftime('%d/%m/%Y')


def nextFriday():
    today = pendulum.now()
    nextMonday = today.next(pendulum.MONDAY).strftime('%Y%m%d')
    nextWedday = today.next(pendulum.WEDNESDAY).strftime('%Y%m%d')
    nextFriday = today.next(pendulum.FRIDAY).strftime('%Y%m%d')
    return nextFriday
    
def nextExpiry():
    expiry = today = pendulum.now()
#    if(today is Monday)
#       expiry = Monday
#   else(today is tues or Wednes)
#       expiry = Wednesday
#   else (today is thurs or friday)
#       expiry = Friday
    return expiry

def validStrike():
    sp = 4600
    return sp

action = "sell"
putcall = "C"
#1 Read current value of ES from yahoo or IB,
#2 Ceil/Floor to +/-5 or +/-10 valid strike
strike = validStrike()       #choose ATM
expr = nextFriday()

#execute the classes
def main():
#create Position (Mon, Wed, Fri)
    #Long NQ
#     app = buyES()
#     app.nextOrderId = 0
#     app.connect("127.0.0.1", port, 9)  # IB Gateway PaperTrading
#     Timer(3, app.stop).start()
#     app.run()

    #sell ATM call, next Expiry
#     app1 = EScall()
#     app1.nextOrderId = 0
#     app1.connect("127.0.0.1", port, 9)  # IB Gateway PaperTrading
#     Timer(3, app1.stop).start()
#     app1.run()

    print(strike)

if __name__ == "__main__":
    main()
