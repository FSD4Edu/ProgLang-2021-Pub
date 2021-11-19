def dollar_to_yen(dollar,rate):
    return dollar * rate
my_d = 100
ur_d = 120
r_yesterday = 105
r_today = 102
print("昨日のレートで私が所持するドルは", dollar_to_yen(my_desterday), "円")
print("昨日のレートで君が所持するドルは", dollar_to_yen(ur_desterday), "円")
print("今日のレートで私が所持するドルは", dollar_to_yen(my_d,r_today), "円")
print("今日のレートで君が所持するドルは", dollar_to_yen(ur_d,r_today), "円")
