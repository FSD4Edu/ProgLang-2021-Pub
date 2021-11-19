def test4(lst1):
    print("lst1-before:", id(lst1))
    lst1[0] = 0
    lst1.append(100)
    print("lst1-after:", id(lst1))
lst2 = [1, 2, 3]
test4(lst2)
print(lst2)
