from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
from threading import Timer
from datetime import datetime
import yfinance as yf
import pandas as pd
import pendulum
#https://pendulum.eustace.io

#port = 7497  # Simulated + TWS
port = 4002 # Simulated + Gateway

ETF = Contract()
ETF.symbol = 'QQQ'
ETF.secType = 'STK'
ETF.exchange = 'GLOBEX'
ETF.currency = 'USD'

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

class SellNQcall(EWrapper, EClient):

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
        contract.symbol = "NQ"
        contract.secType = "FOP"
        contract.exchange = "GLOBEX"
        contract.currency = "USD"
        contract.multiplier = "20" #20 for NQ, 50 for ES

        #place the order
        order = Order()
        order.action = "sell"
        contract.right = "C"
        contract.strike = 14000
        contract.lastTradeDateOrContractMonth = "20210917"
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
#    return expiry

def validStrike():
    str_p = 4600
    ticker = yf.Ticker('ES=F')
    hist = ticker.history(period="3d", interval="5m")
    # print(hist)

    df_history = pd.DataFrame(hist)
    # how to print df_history, on screen or to_csv()

    # pull recent_value from hist
    recent_value = df_history['Close'].iloc[-1]
    print("recent", recent_value)

    #currently find ATM strike by rounding off to closest multiple of 10, which is lower than stock price
    #To do, find the valid strike ATM/ITM or OTM from the options chain
    recent_rounded = recent_value - (recent_value%10)

    return recent_rounded

def OTMStrike():
    return (validStrike() + 10)

action = "buy"
putcall = "C"
#1 Read current value of ES from yahoo or IB,
#2 Ceil/Floor to +/-5 or +/-10 valid strike

#strike = validStrike()       #choose ATM
strike = validStrike()        #OTM (ATM + 10)
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
    app1 = EScall()
#    app1 = SellNQcall()
    app1.nextOrderId = 0
    app1.connect("127.0.0.1", port, 9)  # IB Gateway PaperTrading
    Timer(3, app1.stop).start()
    app1.run()

    print("ATM strike = ", strike )

if __name__ == "__main__":
    main()
