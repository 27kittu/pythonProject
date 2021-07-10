from module1 import *

trades = int(input('Please enter the number of trades: '))
i = 1
while i < trades + 1:
    print('Please enter the trade details as buy rate, sell rate, lot size respectively')
    brate = float(input("buy rate: "))
    srate = float(input("sell rate: "))
    lots = int(input("lot size: "))
    lst_inputs = "lst_input"+str(i)
    lst_inputs= [brate, srate, lots]
    #bro_billing(lst_inputs)
    i+=1
