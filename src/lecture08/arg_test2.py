def test2(num):
    print("num-id:", id(num))
    num += 10
    print("num-id:", id(num))
n = 3
test2(n)
print(n)
print("n-id:", id(n))
