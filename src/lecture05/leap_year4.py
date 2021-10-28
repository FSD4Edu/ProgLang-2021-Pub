year = int(input("西暦を入力してください："))
leapyear = False
leapyear = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
if leapyear == True:
    print(str(year) + "年は閏年です")
else:
    print(str(year)+ "年は平年です")
