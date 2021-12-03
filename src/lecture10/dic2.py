fruits = { # 辞書型のデータは複数行にまたがって記述する事も可能
    "バナナ":300, "オレンジ":240,
    "イチゴ":350, "マンゴー":400}
for name, price in fruits.items():
    print(name + "は" + str(price) + "円です")
