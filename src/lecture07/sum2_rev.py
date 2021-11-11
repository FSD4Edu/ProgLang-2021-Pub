end = int(input("最後の数値を入力してください："))
sum = 0
counter = 1
while counter <= end:
    sum += counter
    counter += 1
print(str(end) + "までの総和：", sum)
