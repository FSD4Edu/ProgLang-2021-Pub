def func1(arglst):
    print("id-bfr@func1:", id(arglst))
    arglst[0] += 10
    print("id-aft@func1:", id(arglst))
def func2(arglst):
    print("id-bfr@func2:", id(arglst))
    arglst = [3, 4, 5]
    print("id-aft@func2:", id(arglst))
def func3(argnum):
   print("id-bfr@func3:", id(argnum))
   argnum += 10
   print("id-aft@func3:", id(argnum))
lst = [0, 1, 2]
num = 10
func1(lst)
print(lst)
func2(lst)
print(lst)
func3(num)
