min = int(input("非負の整数を入力してください："))
max = 2 * min
sum = 0
for num in range(min,max+1):
    if num % 2 == 1:
        continue
    if num >= 10:
        break
    print(str(num), end = " ")
    sum += num
print("[結果] " + str(su
