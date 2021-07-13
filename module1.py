def brokerage_charges(buy_r, sell_r, brokerages):
    Brokerage = brokerages
    IGST_On_Brokerage = (Brokerage * (18 / 100))
    STT_SQUP = round(((0.05 * sell_r) / 100))
    TRANSACTION_CHARGES = (buy_r + sell_r) * (0.05 / 100)
    clearing_charges = (buy_r + sell_r) * (0.005 / 100)
    SEBI_FEES = 0.000001 * sell_r
    IGST_On_Charges = (TRANSACTION_CHARGES + clearing_charges + SEBI_FEES) * (18 / 100)
    return Brokerage, IGST_On_Brokerage, STT_SQUP, TRANSACTION_CHARGES, clearing_charges, SEBI_FEES, IGST_On_Charges

def bro_billing_print(lst):
    print('---------------------------------------------------------------------')
    print('|   s.no  | side(B/S) |   Quantity   |   Net Rate   |    Net Total   |')
    print('----------------------------------------------------------------------')
    i = 0
    summary = []
    total_net_buy = 0
    total_net_sell = 0
    total_buy_lots = 0
    total_sell_lots = 0

    while i < len(lst):
        net_buy = lst[i][0][1] * lst[i][0][0]
        net_sell = lst[i][1][1] * lst[i][1][0]
        total_net_buy = total_net_buy+net_buy
        total_net_sell = total_net_sell+net_sell
        buy_lots = lst[i][0][1]
        sell_lots = lst[i][1][1]
        total_buy_lots = total_buy_lots+buy_lots
        total_sell_lots = total_sell_lots+sell_lots
        total_lots  = total_buy_lots+total_sell_lots
        print('|    {}    |     {}     |     {}    |    {}    |    {}    |'.format(i+1, "B", buy_lots, lst[i][0][0], net_buy))
        print('|    {}    |     {}     |     {}    |    {}    |    {}    |'.format(i+1, "S", sell_lots, lst[i][1][0], net_sell))
        summary.append(lst[i][1][1] * lst[i][1][0]-lst[i][0][1] * lst[i][0][0])
        print('|*SUMMARY*                                 |    *{}*    |'.format(summary[i]))
        i += 1
    count_trades = len(lst)*2
    br_charge = 20
    total_br_charge = 0
    j = 0
    while j<count_trades:
        print('|Brokerage Charges|                         |    {}    |'.format(br_charge))
        total_br_charge= total_br_charge+20
        j+=1

    print('---------------------------------------------------------------------')
    summary_value = 0
    for k in summary:
        summary_value = summary_value + k

    summary_value_final = summary_value-total_br_charge
    print('|   (+) PAY IN/ (-) PAY OUT OBLIGATION          |    {}    |'.format(summary_value_final))
    print('*********************************************************************')
    print()
    charges = brokerage_charges(total_net_buy, total_net_sell, total_br_charge)
    print('                                    |-------------------|')
    print('                                    |  FO-EQ   |  Total |')
    print('                                    |-------------------|')
    print('|PAY IN / ( PAY OUT ) OBLIGATION|            |    {}    |'.format(summary_value_final))
    print("|[IGST 18 percent On Brokerage]|             |    %.3f    |" % charges[1])
    print('|[IGST 18 percent On Charges]|               |    %.3f    |' % charges[6])
    print('[STT-SQUP]                                   |    %.3f    |' % charges[2])
    #print('[STT-RND]                                   |    %.3f    |'.format(charges[]))
    #print('[STAMP DUTY]                                |          |'.format())
    print('[TRANSACTION CHARGES*]                       |    %.3f    |' % charges[3])
    print('[CLEARING CHARGES*]                          |    %.3f    |' % charges[4])
    print('[SEBI FEES]                                  |    %.3f    |' % charges[5])