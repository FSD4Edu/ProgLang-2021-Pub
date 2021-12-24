file = open("sample2.txt", "r", encoding = "utf_8")
for idx, line in enumerate(file):
    print("{:4d}:{}".format(idx+1,line), end="")
file.close()
