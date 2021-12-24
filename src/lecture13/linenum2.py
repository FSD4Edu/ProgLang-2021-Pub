file = open("sample2.txt", "r", encoding = "utf_8")
idx = 0
while True:
    line = file.readline()
    if line == "":
        break
    print("{:4d}:{}".format(idx+1,line), end="")
    idx += 1
file.close()
