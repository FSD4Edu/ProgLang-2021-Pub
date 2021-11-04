itr_num = int(input("計算回数？："))
f0, f1 = 0, 1
print(f0, f1, sep = ", ", end = ", ")
for i in range(itr_num):
    f2 = f0 + f1
    f0 = f1
    f1 = f2
    print(f2, end = ", ")
