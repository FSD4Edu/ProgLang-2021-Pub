def dollar_to_yen(dollar,rate=100):
    return dollar * rate
yen = dollar_to_yen(dollar = 100,rate=105)
print("為替レート：", 105)
print(100, "ドルは", yen, "円")
dollar = 120
yen = dollar_to_yen(dollar = dollar)
print("為替レート：", 100)
print(dollar, "ドルは", yen, "円")
