def exchange_money(n):
    amount = 0
    for ten in range(0, int(n/10)+1):
        for five in range(0, int((n-ten*10)/5)+1):
            for two in range(0, int((n - ten*10 - five*5)/2)+1):
                for one in range(0, int((n - ten*10 - five*5 - two*2))+1):
                    if n == ten*10 + five*5 + two*2 + one:
                        amount += 1
    return amount
