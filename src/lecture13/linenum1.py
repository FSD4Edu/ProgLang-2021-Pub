file = open("sample2.txt", "r", encoding = "utf_8")
lines = file.readlines()
for idx, element in enumerate(lines):
    print("{:4d}:{}".format(idx+1,element), end="")
file.close()
