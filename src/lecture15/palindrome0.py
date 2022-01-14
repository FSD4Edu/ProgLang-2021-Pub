def isPal(x):
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False
def silly(n):
    for i in range(n):
        result = []
        elem = input("要素を入力：")
        result.append(elem)
    if isPal(result):
        print("Yes")
    else:
        print("No")
silly(2)
