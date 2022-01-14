def isPal(x):
    temp = x[:]  # スライスでxのコピーを作りtempと結びつける
    temp.reverse()
    print(temp,x)
    if temp == x:
        return True
    else:
        return False
def silly(n):
    result = []
    for i in range(n):
        elem = input("要素を入力：")
        result.append(elem)
    if isPal(result):
        print("Yes")
    else:
        print("No")
silly(int(input("要素数：")))
