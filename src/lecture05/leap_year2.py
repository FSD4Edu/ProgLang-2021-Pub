year = int(input("西暦を入力してください："))
leapyear = False
if year % 400 == 0:
    leapyear = True
elif year % 100 == 0:
    leapyear = False
elif year % 4 == 0:
    leapyear = True
else:
   leapyear = False
if leapyear == True:
   print(str(year) + "年は閏年です")
else:
   print(str(year)+ "年は平年です")
