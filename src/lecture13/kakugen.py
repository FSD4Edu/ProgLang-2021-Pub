import random
file = open("kakugen.txt", "r", encoding = "utf_8")
lines = file.readlines()
kakugen = lines[random.randrange(len(lines))]
print(kakugen, end = "")
