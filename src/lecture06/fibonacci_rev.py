itr_num = int(input("計算回数？："))
f0, f1 = 0, 1
print(f0, end = ", ")
for i in range(itr_num):
    print(f1, end = ", ")
    f0, f1, = f1, f0 + f1
print(f1)
