with open("sample2.txt", "r", encoding = "utf_8") as file:
    for idx, line in enumerate(file):
        print("{:4d}:{}".format(idx+1,line), end="")
