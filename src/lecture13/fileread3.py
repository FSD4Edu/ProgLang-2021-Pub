file = open("sample.txt", "r", encoding = "utf_8")
lines = file.read()
lineslist = lines.split("\n")
for line in lineslist:
    print(line)
