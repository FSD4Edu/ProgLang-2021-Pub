def dollar_to_yen(dollar,rate):
    return dollar * rate
# 引数にリテラルを指定して関数を呼び出す
yen = dollar_to_yen(dollar=100,rate=105)
print("為替レート:", 105)
print(100, "ドルは", yen, "円")
rate = 100
dollar = 150
# 引数に変数を指定して関数を呼び出す
yen = dollar_to_yen(dollar=dollar,rate=rate)
print("為替レート：", rate)
print(dollar, "ドルは", yen, "円")
